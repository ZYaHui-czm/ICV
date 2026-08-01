from operations import *

#验证输入
def get_nums():
    while True:
        try:
            parts = input("请输入").split()

            if len(parts) != 3:
                print("请输入三部分：数字，运算符，数字")
                continue

            a , op , b = parts
            return float(a) , op , float(b)
        except ValueError:
            print("无效输入，请重新输入")

#主函数测试
if __name__ == "__main__":
    a , op , b = get_nums()
    
    if op == '-':
        result = subtract(a, b)
    elif op == '+':
        result = add(a , b)
    elif op == '*':
        result = multiply(a , b)
    elif op == '/':
        result = divide(a , b)
    else:
        print("请输入正确的运算符")

    print(result)