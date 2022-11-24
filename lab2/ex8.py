'''BANK ACCOUNT'''
bank_acc = int(input())
current_currency = input('Choose currency [USD/KZT]: ').upper()

def add_to_bank_account(sum:float):
    global bank_acc
    bank_acc += sum
    return bank_acc

def substract_from_bank_account(sum:float):
    global bank_acc
    bank_acc -= sum
    return bank_acc

def money_conversion(sum:float, cur_from, cur_to):
    if cur_from != cur_to:
        return sum*470 if cur_from=='USD' else sum/470
    else:
        return sum

# testing
print(f"{add_to_bank_account(500)} {current_currency}")
print(f"{substract_from_bank_account(200)} {current_currency}")
print(f"{money_conversion(bank_acc, current_currency, 'KZT')} {current_currency}")