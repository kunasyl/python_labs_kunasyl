from typing import Optional

from exceptions import NotEnoughMoneyException
from models import BankAccount, WalletType
from repositories import BankAccountRepositories

class BankAccountServices:

    repositories: BankAccountRepositories

    def __init__(self, repositories: BankAccountRepositories) -> None:
        self.repositories = repositories

    def create_bank_account(self, name: str, surname: str, account: WalletType) -> None:
        self.repositories.create_bank_account(name=name, surname=surname, account=account)

    def get_bank_account(self, name: str, surname: str, account: WalletType) -> Optional[BankAccount]:
        return self.repositories.get_bank_account(name=name, surname=surname, account=account)

    def get_account_amount(self, bank_account: BankAccount) -> float:
        acc = self.repositories.get_bank_account(name=bank_account.name, surname=bank_account.surname, account=bank_account.account)
        return acc.amount

    def get_str_account_amount(self, bank_account: BankAccount) -> str:
        acc = self.repositories.get_bank_account(name=bank_account.name, surname=bank_account.surname, account=bank_account.account)
        return f'{acc.amount:.2f} {acc.account.value}'

    def add_to_bank_account(self, bank_account: BankAccount, amount: float) -> None:
        self.repositories.add_amount(bank_account=bank_account, amount=amount)
    
    def substract_from_bank_account(self, bank_account: BankAccount, amount: float) -> None:
        self.repositories.substract_amount(bank_account=bank_account, amount=amount)

    def money_convertion(self, amount: float, acc1: WalletType, acc2: WalletType) -> str:
        new_amount = amount

        if acc1 != acc2:        
            match (acc1, acc2):
                case WalletType.KZT, WalletType.USD:
                    new_amount = amount / 470
                case WalletType.KZT, WalletType.RUB:
                    new_amount = amount / 6
                case WalletType.KZT, WalletType.EUR:
                    new_amount = amount / 490
                case WalletType.RUB, WalletType.KZT:
                    new_amount = amount * 6
                case WalletType.RUB, WalletType.EUR:
                    new_amount = amount / 65
                case WalletType.RUB, WalletType.USD:
                    new_amount = amount / 62
                case WalletType.USD, WalletType.KZT:
                    new_amount = amount * 470
                case WalletType.USD, WalletType.RUB:
                    new_amount = amount * 62
                case WalletType.USD, WalletType.EUR:
                    new_amount = amount / 1.05
                case WalletType.EUR, WalletType.USD:
                    new_amount = amount * 1.05
                case WalletType.EUR, WalletType.RUB:
                    new_amount = amount * 65
                case WalletType.EUR, WalletType.KZT:
                    new_amount = amount * 490
        
        return new_amount

    def send_converted_money(self, amount: float, sender: BankAccount, addresser: BankAccount) -> None:
        try:
            if self.get_account_amount(sender) < amount:
                raise NotEnoughMoneyException
            else:
                self.substract_from_bank_account(bank_account=sender, amount=amount)
                
                converted_money = self.money_convertion(amount=amount, acc1=sender.account, acc2=addresser.account)
                self.add_to_bank_account(bank_account=addresser, amount=converted_money)
        except NotEnoughMoneyException:
            print('You are poor. Why you want to send money to someone')