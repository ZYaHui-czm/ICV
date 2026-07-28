def class_report(date):
    '''定义分析函数'''
    date_report = {}
    for course , scores in date.items():
        date_report[course] = {
            "avg" : round(sum(scores) / len(scores),1),
            "max" : max(scores)
        }
    '''逐行输出'''
    # for key , value in date_report.items():
    #         print(f'{key} {value}')

    return date_report


if __name__ == "__main__":
    '''给定数据'''
    date = {
        "语文": [80, 85, 90, 88],
        "数学": [92, 78, 85, 90],
        "英语": [88, 92, 79, 85]
    }
    print(class_report(date))
    # class_report(date)