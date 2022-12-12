import sys

from handlers import BankAccountHandlers
from repositories import BankAccountRepositories
from services import BankAccountServices

def init():
    acc_repositories = BankAccountRepositories()
    acc_services = BankAccountServices(repositories=acc_repositories)
    acc_handlers = BankAccountHandlers(services=acc_services)

    while True:
        command = input('''
        Enter command number or enter q (quit) to exit:
        1 - Create new bank account
        2 - Choose bank account\n''')

        if command == 'q':
            sys.exit(0)

        if command == '1':
            name, surname = input('Enter your name and surname: ').split()
            acc_type = input('Choose wallet type [USD, RUB, KZT, EUR]: ')
            acc_handlers.create_new_bank_account(name=name, surname=surname, account=acc_type)

        '''User has only one bank account per wallet type'''
        if command == '2':
            name, surname = input('Enter your name and surname: ').split()
            acc_type = input('Choose wallet type [USD, RUB, KZT, EUR]: ')
            current_acc = acc_handlers.get_bank_account(name=name, surname=surname, account=acc_type)
            if current_acc:
                while True:
                    command = input('''
                    Enter command number or enter q (quit) to go back:
                    1 - Add amount
                    2 - Substract amount
                    3 - Send (with converting) money to another bank account
                    4 - Get info\n''')

                    if command == 'q':
                        break

                    if command == '1':
                        amount = float(input('How much you want to add? '))
                        acc_handlers.add_to_bank_account(bank_account=current_acc, amount=amount)
                        
                    if command == '2':
                        amount = float(input('How much you want to substract? '))
                        acc_handlers.substract_from_bank_account(bank_account=current_acc, amount=amount)

                    if command == '3':
                        addresser_name, addresser_surname = input('Enter addresser name and surname: ').split()
                        addresser_acc = input('Enter what account type you want to convert to [USD, RUB, KZT, EUR]: ')
                        addresser = acc_handlers.get_bank_account(name=addresser_name, surname=addresser_surname, account=addresser_acc)

                        if addresser:
                            sending_money = float(input(f'How much {current_acc.account.value} you want to send? '))
                            send_agreement = input(f'You will be sending {sending_money:.2f} to {addresser.name}. Confirm? [y/n]: ').lower()
                            if send_agreement == 'y':
                                acc_handlers.send_converted_money(amount=sending_money, sender=current_acc, addresser=addresser)
                                print(f'Operation succeeded. {addresser.name} is so lucky!')
                            else:
                                print('Operation was interrupted.')

                    if command == '4':
                        print(f'Your current bank account: {acc_handlers.get_str_account_amount(current_acc)}')
                        

if __name__ == '__main__':
    init()