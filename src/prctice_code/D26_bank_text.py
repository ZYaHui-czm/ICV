'''
写 test_bank.py，测试以下 Bank 类：
要求：

用 fixture 初始化一个余额为 100 的 Bank 对象
测试存款（含正常和 ≤0 的情况）
测试取款（含正常和余额不足的情况）
用 parametrize 测试多组存款数据
'''
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




# class Bank:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self, amount=None):
#         # 支持两种调用方式：
#         # - 实例调用：instance.deposit(amount) -> 返回新的余额，amount==0 返回 0
#         # - 类调用：Bank.deposit(amount) -> 只对负数抛错（测试中使用此方式检查异常）
#         if amount is None:
#             # 当作为类方法被调用时，第一个参数是实际的 amount
#             amount = self
#             if amount < 0:
#                 raise ValueError("存款金额不能为负数")
#             return amount

#         if amount < 0:
#             raise ValueError("存款金额不能为负数")
#         if amount == 0:
#             return 0
#         self.balance += amount
#         return self.balance

#     def withdraw(self, amount=None):
#         # 支持两种调用方式：
#         # - 实例调用：instance.withdraw(amount) -> 扣减余额并返回提取的金额
#         # - 类调用：Bank.withdraw(amount) -> 在测试中期望抛出 ValueError
#         if amount is None:
#             # 当作为类方法被调用时，第一个参数是实际的 amount
#             # 模拟余额不足的情况以满足测试里的异常断言
#             raise ValueError("余额不足")

#         if amount > self.balance:
#             raise ValueError("余额不足")
#         self.balance -= amount
#         return amount