from typing import Optional

from exceptions import InvalidWalletTypeException
from services import BankAccountServices
from models import WalletType, BankAccount


class BankAccountHandlers:

    services: BankAccountServices

    def __init__(self, services: BankAccountServices) -> None:
        self.services = services

    def create_new_bank_account(self, name: str, surname: str, account: str) -> None:
        name = name.strip().capitalize()
        surname = surname.strip().capitalize()
        try:
            self.validate_account_type(account)
            account = WalletType[account.upper()]
            self.services.create_bank_account(name=name, surname=surname, account=account)
        except InvalidWalletTypeException:
            print('Invalid wallet type.')

    def get_bank_account(self, name: str, surname: str, account: str) -> Optional[BankAccount]:
        name = name.strip().capitalize()
        surname = surname.strip().capitalize()
        try:
            self.validate_account_type(account)
            account = WalletType[account.upper()]
            return self.services.get_bank_account(name=name, surname=surname, account=account)
        except InvalidWalletTypeException:
            print('Invalid wallet type.')

    def get_account_amount(self, bank_account: BankAccount) -> str:
        return self.services.get_account_amount(bank_account=bank_account)

    def get_str_account_amount(self, bank_account: BankAccount) -> str:
        return self.services.get_str_account_amount(bank_account=bank_account)

    def add_to_bank_account(self, bank_account: BankAccount, amount:float) -> None:
        self.services.add_to_bank_account(bank_account=bank_account, amount=amount)

    def substract_from_bank_account(self, bank_account: BankAccount, amount:float) -> None:
        self.services.substract_from_bank_account(bank_account=bank_account, amount=amount)

    def send_converted_money(self, amount: float, sender: BankAccount, addresser: BankAccount) -> None:
        try:
            self.validate_account_type(sender.account.value)
            self.validate_account_type(addresser.account.value)
            self.services.send_converted_money(amount=amount, sender=sender, addresser=addresser)
        except InvalidWalletTypeException:
            print('Invalid wallet type.')

    @staticmethod
    def validate_account_type(account: str) -> bool:
        if not account.upper() in WalletType._member_names_:
            raise InvalidWalletTypeException
        return True