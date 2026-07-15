def rank(students , scores):
    '''将成绩大于60的学生与其成绩链接后组为字典'''
    name_score_lst = {name : score for name , score in zip(students , scores) if score > 60}

    '''将字典按照值从大到小排序组为一个新的字典'''
    dictname = dict(sorted(name_score_lst.items(),key=lambda item : item[1],reverse=True))

    '''分别定义列表用来存储键和值'''
    namelist = [key for key in dictname]
    scorelist = [value for value in dictname.values()]

    '''用zip将键和值链接，再用enumerate从1开始排名，组为一个字典'''
    dict_name_score = {x : y for x , y in enumerate(zip(namelist,scorelist),1)}
    
    return dict_name_score

if __name__ == "__main__":
    students = ["小明", "小红", "小刚", "小丽"]
    scores = [85, 92, 55, 78]
    print(rank(students , scores))
