from operations import add,subtract,multiply,divide


OPS = {
    '+' : add,
    '-' : divide,
    '*' : multiply,
    '/' : divide
}

def get_nums():
    '''验证输入是否正确及验证运算符'''
    while True:
        try:
            parts = input("请输入:(以空格分隔如：1 + 1)").split()

            if len(parts) != 3:
                print("请输入三部分：数字，运算符，数字")
                continue

            a , op , b = parts

            if op not in OPS:
                print(f'请输入有效的运算符,支持{','.join(OPS)}')
                continue

            return float(a) , op , float(b)
        except ValueError:
            print("无效输入，请重新输入:")

def calculat(a , op , b):
    if op == '/' and b == 0:                        #判断除数不能为零
        raise ZeroDivisionError("除数不能为零!")
    return OPS[op](a , b)                           #调用相应函数计算并返回计算结果

#主函数测试
if __name__ == "__main__":
    while True:
        '''确保不因除以零而提前结束'''
        try:
            a , op , b = get_nums()
            result = calculat(a , op , b)
            print(result)
        except ZeroDivisionError as e:
            print(e)

        if input("继续请回车，退出请输入q:").lower() == 'q':
            break