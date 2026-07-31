'''
写一个生成器函数 chunked(lst, size)：

接收一个列表和分块大小
每次 yield 出 size 大小的子列表
最后一块不够 size 就直接返回剩余部分
'''
def chunked(lst , size):
    for i in range(0,len(lst) , size):
        yield lst[i:i + size]


for chunk in chunked([1, 2, 3, 4, 5, 6, 7], 3):
    print(chunk)