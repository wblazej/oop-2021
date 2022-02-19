import hashlib
from dataclasses import dataclass
import string
import aiohttp
import asyncio
import os
from dotenv import load_dotenv
from asyncache import cached
from cachetools import TTLCache

@dataclass
class WdToken:
    studentid: int
    wdauth: str
    expiry_epoch_s: int

@dataclass
class User:
    student_id: int
    album: string
    name: str
    surname: str

    @staticmethod
    def from_dict(d: dict):
        return User(
            student_id=d['studentid'],
            album=d['album'],
            name=d['imie'],
            surname=d['nazwisko']
        )

class UnauthorizedError(BaseException):
    def __str__(self) -> str:
        return 'Wrong username or password :/'

class UnknownError(BaseException):
    pass

class UserService:
    async def login_user(self, album: str, password: str) -> WdToken:
        _hash = await self.__hash_password(password)
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://wdauth.wsi.edu.pl/authenticate?album={album}&pass={_hash}') as resp:
                if (resp.status == 200):
                    data = await resp.json()
                    return WdToken(studentid=data['token']['studentid'], 
                                    wdauth=data['token']['wdauth'], 
                                    expiry_epoch_s=data['token']['expiry_epoch_s'])
                elif (resp.status == 401):
                    raise UnauthorizedError
                else:
                    raise UnknownError

    @cached(TTLCache(100, 180))
    async def get_user(self, wdauth: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://wdauth.wsi.edu.pl/user?wdauth={wdauth}') as resp:
                user_data = await resp.json()
                return User.from_dict(user_data)

    async def __hash_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()

async def main():
    load_dotenv()
    correct_password = os.getenv('correct_password')
    incorrect_password = os.getenv('incorrect_password')
    
    try:
        user_service = UserService()
        auth = await user_service.login_user('U/11', correct_password)

        user = await user_service.get_user(auth.wdauth)
        print(user)
    except UnauthorizedError as e:
        print(str(e))

asyncio.run(main())
