def chunked(lst , size):
    for i in range(0,len(lst) , size):
        yield lst[i:i + size]


for chunk in chunked([1, 2, 3, 4, 5, 6, 7], 3):
    print(chunk)