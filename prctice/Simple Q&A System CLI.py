question1 = {
    'question' : 'Python的创始年份是？',
    'options' : {"A": "1989", "B": "1991", "C": "2000", "D": "2008"},
    'answer' : 'B'
}

question2 = {
    'question' : '以下哪个是可变数据类型？',
        'options' : {"A": "str", "B": "int", "C": "list", "D": "tuple"},
        'answer' : 'C'
}
question3 = {
    'question' : 'len("Python") 的结果是？',
        'options' : {"A": "5", "B": "6", "C": "7", "D": "8"},
        'answer' : 'B'
}

questions = [question1,question2,question3]

def run_QA (questions):
    '''运行cli'''
    score = 0
    total = len(questions)
    for i , q in enumerate(questions,1):
        print(f'\nNo.{i}question:{q['question']}')
        for key , value in q['options'].items():
            print(f'{key}.{value}')

        '''获取输入'''
        user_answer = input('please answer:').strip().upper()

        '''判断是否为无效输入'''
        while user_answer not in q['options']:
            user_answer = input('Error!please answer again:').strip().upper()

        if user_answer == q['answer']:
            print('right!')
            score += 1
        else:
            print(f'error!The correct answer is {q['answer']}')
    return score , total

'''调用函数'''
if __name__ == '__main__' :
    correct , total =run_QA(questions)
    print(f'\nYou got {correct} questions right')
    print(f'Accuracy rate {correct / total * 100:.1f}%')