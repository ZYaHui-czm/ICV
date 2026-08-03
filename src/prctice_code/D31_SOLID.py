'''
重构下面的代码，让它同时符合单一职责 + 开闭 + 依赖倒置：

# 原始代码（需要重构）
class OrderProcessor:
    def __init__(self):
        self.logger = FileLogger()     # 直接依赖具体类
    def process(self, order):
        # 处理订单
        self.logger.log_to_file(f"处理订单 {order.id}")
        # 计算折扣
        if order.total > 100:
            discount = 0.1
        else:
            discount = 0
        # 发送邮件
        self.send_email(order)

要求：

定义抽象接口 Logger，具体类 FileLogger 实现它
OrderProcessor 依赖 Logger 接口（依赖倒置）
拆分成单一职责（订单计算、日志、通知分开）
开闭原则：加新通知方式不用改 OrderProcessor
'''


from abc import ABC , abstractmethod

#===========定义抽象接口===========

class Logger(ABC):
    @abstractmethod
    def log(self , order):
        ...

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self , amount):
        ...

class MessageSender(ABC):
    @abstractmethod
    def send(self , message):
        ...

#========定义具体方法===========
class FileLogger(Logger):
    def log(self, order):
        print(f'[日志]{order}')

class DiscountOver100(DiscountStrategy):
    def calculate(self , amount):
        if amount > 100:
            return amount*0.9
        return amount

class DefaultPay(DiscountStrategy):
    def calculate(self , amount):
        return amount

class EmailSend(MessageSender):
    def send(self, message):
        print(f'email:{message}')


#======依赖倒置===========
class OrderProcessor:
    def __init__(
            self,
            logger: Logger,
            discount: DiscountStrategy,
            sender: MessageSender
    ):
      self.logger = logger
      self.discount = discount
      self.sender = sender

    def process(self , order):
        #日志
        self.logger.log(f'处理订单{order['id']}')

        #计算折扣
        final_price = self.discount.calculate(order['total'])

        #发送通知
        self.sender.send(f'订单{order['id']}已处理,金额{final_price:.2f}')

        return final_price


#=======接口注入=========
if __name__ == "__main__":
    order = {
        'id': 851,
        'total': 248
    }

    project1 = OrderProcessor(
        logger=FileLogger(),
        discount=DiscountOver100(),
        sender=EmailSend()
    )
    project1.process(order)