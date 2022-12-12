class BankAccountDoesntExistException(Exception):
    "Raised when the specified bank account does not exist"
    pass

class InvalidWalletTypeException(Exception):
    "Raised when the specified wallet type does not exist"
    pass

class NotEnoughMoneyException(Exception):
    "Raised when you are poor"
    pass