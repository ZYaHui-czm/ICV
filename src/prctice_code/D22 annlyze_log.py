'''
用 Counter 写一个函数 analyze_log(log_text)：

统计每个单词的出现次数
找出出现次数最多的 5 个单词（忽略大小写）
返回格式：[("word", count), ...]
'''
from collections import Counter

def analyze_log(log_text):
    # lit_log = list(log_text.lower().split())      #从列表中获取
    count = Counter(log_text.lower().split())       #从字符串中获取
    return count.most_common(5)

if __name__ == "__main__":
    log = "ERROR server down ERROR timeout WARNING disk full ERROR timeout timeout INFO started"
    print(analyze_log(log))