from functools import wraps
from datetime import datetime , timedelta

def count_calls(func):
    count = 0

    @wraps(func)
    def wrapper(*args):
        nonlocal count              #指代外层变量，global指代全局变量
        result = func(*args)
        for item in result:         #使用生成器函数拦截每次yield
            count += 1
            yield item
        print(f'总共执行了{count}次next()')
    return wrapper

@count_calls
def date_range(start_date , end_date):
    start = datetime.strptime(start_date , "%Y-%m-%d")      #.strptime是将字符串转换为datetime，p=parse(解析/读入)
    end = datetime.strptime(end_date , "%Y-%m-%d")
    current = start
    while current <= end:
        yield current.strftime("%Y-%m-%d")                  #.strftime是将datetime转换为字符串，f=format(格式化/输出)
        current += timedelta(days=1)

'''生成器调用不执行，需要用for循环或者next()手动测试'''
for data in date_range("2025-07-01" , "2025-07-05"):
    print(data)
'''
for循环调用生成器:
while True:
    try:
        date = next(result)     #逐个取值，需要才给
        print(date)
    except StopIteration:       #取完结束
        break
'''