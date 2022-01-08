from random import randint
from file_based_logger import FileBasedLogger
from decorstors import logged, retry, unsafe


custom_logger = FileBasedLogger('a.log')
custom_logger.open_file()


class BankAPIError(BaseException):
    pass


@unsafe(ignored_errors=BankAPIError)
@retry(attempts=3, delay=2, backoff_type='exponential')
@logged(custom_logger=custom_logger)
def transfer_money(bank1: str, bank2: str, amount: float):
    if randint(0, 5) != 0:
        raise BankAPIError

    print(f'Tranferred {amount} PLN from {bank1} to {bank2}')


if __name__ == "__main__":
    transfer_money("MBank", "ING", 245.31)
