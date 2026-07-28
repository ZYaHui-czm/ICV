from collections import Counter

def analyze_log(log_text):
    # lit_log = list(log_text.lower().split())      #从列表中获取
    count = Counter(log_text.lower().split())       #从字符串中获取
    return count.most_common(5)

if __name__ == "__main__":
    log = "ERROR server down ERROR timeout WARNING disk full ERROR timeout timeout INFO started"
    print(analyze_log(log))