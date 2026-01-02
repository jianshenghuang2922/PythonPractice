import json
import os
data = {"owner":"jiansheng","balance": 1000}
class BankAccount:
    def __init__(self,owner,balance=None):
        self.owner = owner
        self._balance = balance if balance else 0
    
    def save_to_file(self):
        data = {
            "owner": self.owner,
            "balance": self._balance
        }
       
        with open("account.json",'w',encoding = 'utf-8') as f:
            json.dump(data,f,indent = 4)
            print("----数据已存档----")
       
    def load_from_file(self):
        with open("account.json",'r',encoding = 'utf-8') as f:
            data = json.load(f)
            self.owner = data["owner"]
            self._balance = data["balance"]
            print(f"---- 成功读档：欢迎回来 {self.owner}, 当前余额：{self._balance}----")
    def deposit(self,amount):
    
        if amount < 0:
            raise ValueError("请输入不小于0的金额")
        else:
            self._balance += amount
            print(f"存入{amount} 元， 当前余额：{self. _balance}")
        
    def withdraw(self,amount):    
        if amount < 0:
            raise ValueError("输入金额不能小于0")
        elif self._balance>=amount:
            self._balance -= amount
            print(f"当前余额为：{self._balance}")
        else:
            raise RuntimeError(f"余额不足,取款失败")
        
    def show_balance(self):
        print(f"当前余额为：{self._balance}")
    def month_report(self):
        print(f"[持有人]: {self.owner}, 请注意查看本月账单")
class SavingAccount(BankAccount):
    
    def __init__(self,owner,balance = 0,interest_rate = 0.01):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
  
    def add_interest(self):
        self.interest = self._balance * self.interest_rate
        self._balance += self.interest

class CreditAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate = 0.02):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.interest = self._balance * self.interest_rate
        self._balance += self.interest
accounts = [
    BankAccount("jiansheng",100),
    SavingAccount("yanbo",1000,0.05),
    CreditAccount("LiMing",-500)
]
user = SavingAccount("LiMing",0)
user.load_from_file()
while True:
    user.save_to_file()
    choice = input("是否要继续存款 (Y/N): ").upper()
    if choice == 'N':
        break
    try:
        amount = float(input("请输入存款金额: ") )  
    except ValueError:
        print("请输入有效值")
        continue
    user.deposit(amount)
    
    
    


