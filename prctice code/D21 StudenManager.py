class StudentManager:
    '''初始化'''
    def __init__(self):
        self.students = {}

    '''添加学生'''
    def add(self , name , score):
        self.students[name] = score

    '''去除'''
    def remove(self , name):
        if name in self.students:
            del self.students[name]

    '''获取成绩从高到低的前n名学生的名字'''
    def top(self , n):
        self.top_student = dict(sorted(self.students.items() , key = lambda x : x[1] , reverse = True))
        return list(self.top_student)[:n]
        # print(list(top_student)[:n])

    '''保存为json文件'''
    def save(self , filename):
        import json
        with open(filename , "w" , encoding="utf-8") as f:
            json.dump(self.students , f ,ensure_ascii=False , indent=2)

    '''读取json文件'''
    def load(self , filename):
        import os
        import json
        if os.path.exists(filename):
            with open(filename , "r" , encoding="utf-8") as f:
                self.students = json.load(f)
        else:
            self.students = []

    '''计算长度'''
    def __len__(self):
        return len(self.students)

# 测试
if __name__ == "__main__":
    l = StudentManager()
    l.add('xiaom' , 88)
    l.add("ssss" , 90)
    l.add("wwww" , 100)
    print(l.students)
    print('-'*30)
    print(len(l))
    print('-'*30)
    l.remove("xxx")
    print(l.students)
    print('-'*30)
    print(l.top(2))
    print('-'*30)
    l.save("student.json")
    l2 = StudentManager()
    l2.load("student.json")
    print(l2.students)