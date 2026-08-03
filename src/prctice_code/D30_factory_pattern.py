'''
用工厂模式实现一个通知系统：

EmailNotifier, SMSNotifier, PushNotifier 三个类，都有 send(msg) 方法
每个 send 打印不同的内容
NotifierFactory.create(type) 根据类型返回对应通知器
未知类型抛 ValueError
'''

#不需要初始化类
class EmailNotifier:

    def send(self , msg):
        print(f'email:{msg}')

class SMSNotifier:

    def send(self , msg):
        print(f'SMS: {msg}')

class PushNotifier:

    def send(self , msg):
        print(f'Push :{msg}')

class NotifierFactory:
    _PushType = {
        "email": EmailNotifier,
        "sms": SMSNotifier,
        "push": PushNotifier
    }

    #有cls需要classmethod
    @classmethod
    def create(cls , notify_type):
        push_type = cls._PushType.get(notify_type)
        if push_type is None:
            raise ValueError(f'未知通知类型:{notify_type}')
        return push_type()


#测试
n1 = NotifierFactory.create('email')
n1.send('steam:你的交易....')

n2 = NotifierFactory.create('sms')
n2.send('你的steam修改密码验证码:114514')

n3 = NotifierFactory.create('push')
n3.send('你有一条新的steam消息')

NotifierFactory.create('wechat')