def pheon_book(name):
    pbook = {
        'Alex' : '11111',
        'Deram' : '25468',
        'Tom' : '4678964',
        'Steve' : '564982313'
    }

    # index_name = input("Who do you want to see :")
    if index_name not in pbook:
        print("Not found!")
    else:
        print(f'The phone nomber is : {pbook[index_name]}')

if __name__ == "__main__":
    index_name = (input("Who do you want to see :"))
    pheon_book(index_name)