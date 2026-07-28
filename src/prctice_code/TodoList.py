class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self , task):
        self.tasks.append(task)
        print(f'已添加:{task}')

    def remove(self , task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'已完成:{task}')
        else:
            print(f'未找到:{task}')

    def show(self):
        for i , t in enumerate(self.tasks , 1):
            print(f'{i}.{t}')


'''测试'''
t1 = TodoList()
t1.add("学习")
t1.add("to study icv")
t1.add("11111")
t1.show()
t1.remove("做作业")
t1.remove("11111")
t1.show()