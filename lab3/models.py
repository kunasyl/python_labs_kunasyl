from enum import Enum
import hashlib


class WalletType(Enum):
    USD = 'USD'
    RUB = 'RUB'
    KZT = 'KZT'
    EUR = 'EUR'

    
class BankAccount:
    name: str
    surname: str
    account: WalletType
    __amount: float

    def __init__(self, name: str, surname: str, account: WalletType):
        self.name = name
        self.surname = surname
        self.account = account

    @property
    def amount(self) -> float:
        return self.__amount
        
    def set_amount(self, amount: float):
        self.__amount = amount

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} has {self.__amount} {self.account.value}'

    def __del__(self):
        print('Bank account was deleted')