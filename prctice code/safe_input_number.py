def safe_input_number():
    '''定义函数'''
    while True:
        '''捕获异常'''
        try:
            prompt = int(input())
            print(prompt)
        except:
            print("please enter a valid number!")
        else:
            break

if __name__ == "__main__":
    print("please enter a number:")
    safe_input_number()