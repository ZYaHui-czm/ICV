def best_course(data):
    '''统计每门课程的平均分和最高分'''
    grade_analyz = {}
    for course , scores in data.items():
        grade_analyz[course] = {
            "平均" : round(sum(scores) / len(scores),1),
            "最高" : max(scores),
        }

    '''打印统计信息'''
    for course , value in grade_analyz.items():
        print(f'{course}:平均{value["平均"]},最高{value["最高"]}')

    '''查找平均分最高的课程'''
    '''max()的参数是字典时,遍历的是键。
    key参数(自定义比较规则)决定按什么标准比较,lambda函数获取返回每门课平均分对于的值并让max()以该值为准比较'''
    best_name = max(grade_analyz,key= lambda x : grade_analyz[x]["平均"])
    print(f'平均分最高：{best_name}')

if __name__ == "__main__":
    data = {
        "语文": [80, 85, 90],
        "数学": [92, 88, 95],
        "英语": [78, 82, 80]
    }
    best_course(data)