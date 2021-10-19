import rsa

class Account:
    __website: str
    __login: str
    __password: bytes

    def __init__(self, website: str, login: str, password: str, public_key: rsa.PublicKey):
        self.__website = website
        self.__login = login
        self.__password = rsa.encrypt(password.encode(), public_key)

    def __repr__(self):
        return f'Website: {self.__website}, Login: {self.__login}'

    def get_credentials(self, private_key: rsa.PrivateKey):
        return (self.__login, rsa.decrypt(self.__password, private_key).decode())

    @property
    def website(self):
        return self.__website

    @property
    def login(self):
        return self.__login
