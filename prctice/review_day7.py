def analyze_text(text):
    '''定义分析函数'''
    text_ana = {
        'length' : len(text),
        'upper_text' : text.upper(),
        'words' : len(text.split()),
        'reversed' : text[::-1]
    }

    '''获取键和值'''
    for key ,value in text_ana.items():
        print(f'{key} : {value}')

    return text_ana

if __name__ == "__main__":
    '''调用函数'''
    text = input()
    analyze_text(text)