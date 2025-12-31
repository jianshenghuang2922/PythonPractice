import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit",self)
        self.initUI()
    def initUI (self):
        self.line_edit.setGeometry(10,10,300,40)
        self.button.setGeometry(320,10,100,40)
        self.line_edit.setStyleSheet("font-size:25px;"
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial;"
                                  )
        self.line_edit.setPlaceholderText("Enter your name")
        self.button.clicked.connect(self.submit)
    def submit(self):
        text= self.line_edit.text()
        print(f" {text}")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())