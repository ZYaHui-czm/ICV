# nums = [3, 1, 4, 1, 5, 9, 2, 6]

# print(nums.sort())

"""
双色球随机选号程序

Author: 骆昊
Version: 1.0
"""
# import random

# red_balls = list(range(1, 34))
# selected_balls = []
# # 添加6个红色球到选中列表
# for _ in range(6):
#     # 生成随机整数代表选中的红色球的索引位置
#     index = random.randrange(len(red_balls))
#     # 将选中的球从红色球列表中移除并添加到选中列表
#     selected_balls.append(red_balls.pop(index))
# # 对选中的红色球排序
# selected_balls.sort()
# # 输出选中的红色球
# for ball in selected_balls:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# # 随机选择1个蓝色球
# blue_ball = random.randrange(1, 17)
# # 输出选中的蓝色球
# print(f'\033[034m{blue_ball:0>2d}\033[0m')

# a, b, *c = range(1, 10)
# print(a, b, c)
# a, b, c = [1, 10, 100]
# print(a, b, c)
# a, *b, c = 'hello'
# print(a, b, c)
# 问题1：这个"计时器"有什么bug？
import time
def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print(time.time() - start)
        return result
    return wrapper

@timer
def greet(user):
    return f"你好，{user}"

@timer
def add(a, b):
    return a + b

print(greet("小明"))
print(add(3, 5))

# 问题2：预期输出 0,1,2，实际输出什么？为什么？
def counter():
    n = 0
    while n < 3:
        yield n
        n += 1

c = counter()
print(list(c))
print(list(c))