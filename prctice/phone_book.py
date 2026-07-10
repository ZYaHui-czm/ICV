def phone_book(contact_name):
    pbook = {
        'Alex' : '11111',
        'Deram' : '25468',
        'Tom' : '4678964',
        'Steve' : '564982313'
    }

    # contact_name = input("Who do you want to see :")
    if contact_name not in pbook:
        return "Not found!" 
    return f'The phone number is : {pbook[contact_name]}'

if __name__ == "__main__":
    contact_name = (input("Who do you want to see :"))
    print(phone_book(contact_name))