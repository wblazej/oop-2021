from dataclasses import dataclass
from typing import Iterable
from unittest.mock import Mock, MagicMock
import unittest
from typing import List


@dataclass
class User:
    id: int
    name: str


class Db:
    """
    Klasa dostępu do storeage'a userów... prawdopodobnie bazy na zewnętrznym serwerze.
    """
    users = List[User]

    def __init__(self) -> None:
        self.users = []

    def get_version(self):
        return '0.0.1'

    def all_users(self) -> Iterable[User]:
        """
        :return: Iterable of all users in the database.
        """
        return self.users
    
    def add_user(self, new_user):
        if not any(u.id == new_user.id for u in self.users):
            self.users.append(new_user)
        else:
            return "ID_DUPLICATED"

    def remove_user(self, id: int):
        for i, o in enumerate(self.users):
            if o.id == id:
                self.users.pop(i)
                break


class AuthChecker:
    db: Db

    def __init__(self, db: Db):
        self.db = db

    def is_user(self, id: int):
        user_ids = [u.id for u in self.db.all_users()]
        return id in user_ids




class DbTests(unittest.TestCase):
    def setUp(self) -> None:
        self.db = Db()
        self.auth = AuthChecker(self.db)

    def test1(self):        
        self.db.all_users = MagicMock(return_value=[])
        self.assertEqual(self.auth.is_user(2), False)

    def test2(self):
        self.db.all_users = MagicMock(return_value=[User(1, 'Kowalski'), User(2, 'Kowalski')])
        self.assertEqual(self.auth.is_user(1), True)
        self.assertEqual(self.auth.is_user(2), True)
        self.assertEqual(self.auth.is_user(3), False)

    def test3(self):
        self.db.add_user(User(2, "test2"))
        self.assertEqual(self.auth.is_user(2), True)

    def test4(self):
        self.db.add_user(User(1, "test1"))
        self.assertEqual(self.db.add_user(User(1, "test2")), "ID_DUPLICATED")

        self.db.add_user(User(2, "test2"))
        self.assertEqual(self.auth.is_user(2), True)

    def test5(self):
        self.db.add_user(User(5, "test"))
        self.assertEqual(self.auth.is_user(5), True)

    def test6(self):
        self.db.add_user(User(1, "test"))
        self.assertEqual(self.auth.is_user(1), True)

        self.db.remove_user(1)
        self.assertEqual(self.auth.is_user(1), False)

if __name__ == '__main__':
    unittest.main()

    # tworzenie kontekstu
    # db = Db()
    # auth = AuthChecker(db)

    # mock-owanie i testowanie
    # print(db.get_version())
    # users = db.all_users()

    # db.all_users = MagicMock(
    #     return_value=[User(2, 'Xi'), User(5, 'Jair')])  # podmieniamy prawdziwą metodę, i piszemy co ma zwrócić

    # db.all_users = MagicMock(return_value=[])
    # print(auth.is_user(2))

    # db.all_users.side_effect = [[User(2,'Xi')], []]   # todo: multiple values

    # print(db.all_users())
    # db.all_users = MagicMock(return_value=[])  # podmieniamy prawdziwą metodę, i piszemy co ma zwrócić
    # print(db.all_users())
    # print(auth.is_user(11))

    # print(db.all_users.mock_calls)  # z tego można zobaczyć jakie zapytania do metody `all_users` zostały wykonane
    # db.all_users.assert_called()    # rzuci błędem, jeśli ta metoda nie została uruchomiona

    # users = db.all_users()
    # print(users)

    # a = AuthChecker(db)
    # print(a.is_user(2))
    # print(a.is_user(3))