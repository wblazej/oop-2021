import rsa
from typing import List
from account import Account

class PasswordManager:
    __public_key: rsa.PublicKey
    __accounts: List[Account]

    def __init__(self, public_key):
        if type(public_key) != rsa.PublicKey:
            raise RuntimeError("Not a public key")
            
        self.__public_key = public_key
        self.__accounts = []

    def add_account(self, website: str, login: str, password: str):
        if self.__is_duplicated(website, login):
            raise RuntimeError("Login duplicated on this website")
        self.__accounts.append(Account(website, login, password, self.__public_key))

    @property
    def accounts(self):
        return self.__accounts

    def get_credentials(self, website: str, private_key: rsa.PrivateKey, login: str = None):
        if type(private_key) != rsa.PrivateKey:
            raise RuntimeError("Not a private key")

        accounts = []
        for acc in self.__accounts:
            if acc.website == website:
                if login:
                    if acc.login == login:
                        return acc.get_credentials(private_key)
                else:
                    accounts.append(acc)

        return [acc.get_credentials(private_key) for acc in accounts]

    def __is_duplicated(self, website, login):
        return not not sum([1 if acc.website == website and acc.login == login else 0 for acc in self.__accounts])
