'''写一个 DataProcessor 类：

__init__(self, filename) — 用 pandas 读取 CSV
filter_column(self, col, threshold) — 筛选出某列大于 threshold 的行（返回 DataFrame）
add_total(self, cols) — 把指定多列相加得到 "总分" 列
group_avg(self, group_col, value_col) — 按 group_col 分组求 value_col 平均
用 __enter__/__exit__ 让这个类支持 with 语句'''

import pandas as pd
class DataProcessor:

    '''主要功能'''
    def __init__(self , filename):
        self.df = pd.read_csv(filename , encoding="utf-8")

    def filter_column(self , col , threshold):
        self.thr = self.df[self.df[col] > threshold]
        # datafra = pd.DataFrame(self.thr)
        return self.thr

    def add_total(self , cols):
        self.df["总分"] = self.df[cols].sum(axis  = 1)
        return self

    def group_avg(self , group_col , value_col):
        return self.df.groupby(group_col , as_index=False)[value_col].mean().round(1)

    '''上下文管理器'''
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.df = None
        return False

#测试
with DataProcessor("students.csv") as dp:
    dp.add_total(["语文", "数学", "英语"])
    print(dp.filter_column("总分", 250))
    print(dp.group_avg("班级", "总分"))