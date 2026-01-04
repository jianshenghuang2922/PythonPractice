import json
from fastapi import FastAPI
from pydantic import BaseModel


data = {"owner":"jiansheng","balance": 1000}
def auto_save(func):
        def wrapper(*args,**kwargs):
            
            results = func(*args,**kwargs)  
            args[0].save_to_file()
            return results
        return wrapper
class AccountAction(BaseModel):
    amount: float
    
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
    @auto_save
    def deposit(self,amount):
    
        if amount < 0:
            raise ValueError("请输入不小于0的金额")
        else:
            self._balance += amount
            print(f"存入{amount} 元， 当前余额：{self. _balance}")
    @auto_save    
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



    
    
app = FastAPI()
user = BankAccount("jiansheng",1000)
user.load_from_file()
@app.get("/account")
def get_account():
    return {"owner": user.owner,"balance": user._balance}

@app.post("/deposit")
def do_deposit(trans: AccountAction):
   
    try:
        user.deposit(trans.amount)
        return {"message": f"存款成功,当前余额： {user._balance}"}
    
    except ValueError as e:
        return {"error": str(e)}
        
@app.post("/withdraw")
def do_withdraw(trans:AccountAction):
    try:
        user.withdraw(trans.amount)
        return {"message": "取款成功","current_balance": user._balance}
    
    except ValueError as e:
        return {"error": str(e)}


