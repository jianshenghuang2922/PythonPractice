import sys
from PyQt5.QtWidgets import QApplication ,QWidget ,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.time = QTimer(self)
        self.initUI()
       

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
                                      "font-size: 150px;"
                                      "font-family: Arial;"
                                      "color: green;")
        self.setStyleSheet("background-color: black")
        self.time.timeout.connect(self.update_time)
        self.time.start()
        self.update_time()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
