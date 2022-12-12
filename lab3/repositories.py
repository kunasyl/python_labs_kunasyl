from typing import Optional

from exceptions import BankAccountDoesntExistException
from  models import BankAccount, WalletType


class BankAccountRepositories:
    accounts: list[BankAccount] = []

    def create_bank_account(self, name: str, surname: str, account: WalletType):
        bank_account = BankAccount(name=name, surname=surname, account=account)
        bank_account.set_amount(amount=0)

        self.accounts.append(bank_account)
        print(f'Congrats, {bank_account.name}, new bank account was created!')

    def get_bank_account(self, name: str, surname: str, account: WalletType) -> Optional[BankAccount]:
        bank_account = next(
            (a for a in self.accounts if name==a.name and surname==a.surname and account==a.account),
            None
        )

        try:
            if not bank_account:
                raise BankAccountDoesntExistException
            else:
                return bank_account
        except BankAccountDoesntExistException:
            print('Selected bank account does not exist')

    def add_amount(self, bank_account: BankAccount, amount: float) -> None:
        bank_account.set_amount(bank_account.amount + amount)

    def substract_amount(self, bank_account: BankAccount, amount: float) -> None:
        bank_account.set_amount(bank_account.amount - amount)