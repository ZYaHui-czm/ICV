class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)

class Library(Store):
    '''子类继承父类所有公开方法和属性，私有成员也会被继承，但是会被改名字'''
    def __init__(self, name):
        super().__init__(name)

    def lend(self , item):
        if item in self.items:
            self.items.remove(item)
            print(f'借出:{item}')
        else:
            print(f'没有:{item}')

    def __str__(self):
        return f'{self.name}图书馆：共{self.count()}本书'


'''测试'''
# l = Library("新华书店")
# l.add("三体")
# l.add("python入门")
# l.add("高等数学")
# print(l)
# print()
# l.lend("大学物理")
# l.lend("高等数学")
# print(l)