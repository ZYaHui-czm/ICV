class Bank:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount