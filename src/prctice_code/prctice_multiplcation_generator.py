'''生成器的简单练习'''
'''通过生成器实现输出某个数的乘法表'''

'''生成器函数实现'''
def multiplcation_generator(x):
    while True:
        for i in range(1 , 9):
            yield f'{i} x {x} = {i * x}'

multi_gen = multiplcation_generator(2)
print(next(multi_gen))
print(next(multi_gen))
print(next(multi_gen))


print('-' * 10)
'''迭代器类实现'''
class Multiplcation_generator():
    def __init__(self , x):
        self.x = x
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        return f'{self.i} x {self.x} = {self.i * self.x}'

mul_gen = Multiplcation_generator(2)
print(next(mul_gen))
print(next(mul_gen))
print(next(mul_gen))