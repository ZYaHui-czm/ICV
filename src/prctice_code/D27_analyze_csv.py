import pandas as pd
def analyze_csv(filepath):
    df = pd.read_csv(filepath , encoding="utf-8")
    df["总分"] = df['语文'] + df['数学'] + df['英语']
    df["平均分"] = df['总分'].mean().round(1)
    df_gro = df.groupby('班级')['总分'].mean()
    # df_gro = df.groupby('班级' , as_index=False)['总分'].mean().rename(columns = {"总分":"平均分"})       #将输出带上表头(把索引改为列)
    # df_gro = df.groupby('班级' , as_index=False).agg(平均分 = ("总分" , "mean"))                          #将输出带上表头(把索引改为列)
    # print(df_gro)
    return df_gro

if __name__ == "__main__":
    result = analyze_csv('students.csv')
    print(result)