def class_report(date):
    '''定义分析函数'''
    for key in date:
        date_report = {
            "avg" : sum(date[key]) / len(date[key]),
            "max" : max(date[key])
        }
    '''逐行输出'''
    for key in date:
        print(f'The {key} :')
        for key , value in date_report.items():
                print(f'    The {key} is {value}')

    # return date_report


if __name__ == "__main__":
    '''给定数据'''
    date = {
        "语文": [80, 85, 90, 88],
        "数学": [92, 78, 85, 90],
        "英语": [88, 92, 79, 85]
    }
    # print(class_report(date))
    class_report(date)