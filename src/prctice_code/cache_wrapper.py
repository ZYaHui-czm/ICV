from functools import wraps

def cache(func):
    memory = {}

    @wraps(func)
    def wrapper(*args):
        if args in memory:          #先查缓存是否在memory
            return memory[args]     #在直接返回缓存不在计算
        result = func(*args)        #没算过的计算
        memory[args] = result       #存入缓存
        return result
    return wrapper

# 测试
@cache
def fib(n):
    # print(f'计算{n}')             #检验装饰器是否生效
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # 应该很快算出55