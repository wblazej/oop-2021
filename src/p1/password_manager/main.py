import rsa
from password_manager import PasswordManager

if __name__ == "__main__":

    public_key, private_key = rsa.newkeys(512)

    manager = PasswordManager(public_key)

    manager.add_account("google.com", "test1@gmail.com", "Haslo123")
    manager.add_account("google.com", "test2@gmail.com", "Haslo123")

    print(manager.get_credentials("google.com", private_key, login="test1@gmail.com"))
