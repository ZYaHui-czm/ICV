'''写一个函数 pair_sums(nums)：
用 itertools.combinations 找出列表中所有两个不同位置元素的组合
计算每组组合的和
用 Counter 统计每种和的出现次数
返回出现最多的和及其次数'''


from itertools import combinations
from collections import Counter

def pair_sums(nums):
    num_combin = combinations(nums , 2)
    # sum_lst = []                              #for循环实现
    # for a,b in num_combin:
    #     sum_lst.append(a + b)

    sum_lst = [a + b for a , b in num_combin]   #列表生成式实现
    nums = Counter(sum_lst)
    return nums.most_common(1)[0]               #不加[0]返回的是[(5,2)]，加上返回裸元组

# a = [1,2,3,4]
#测试
if __name__ == "__main__":
    print(pair_sums([1,2,3,4]))