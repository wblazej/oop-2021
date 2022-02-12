import hashlib
from dataclasses import dataclass
import aiohttp
import asyncio
import os
from dotenv import load_dotenv

@dataclass
class WdToken:
    studentid: int
    wdauth: str
    expiry_epoch_s: int

@dataclass
class User:
    name: str
    surname: str
    created_at: str
    active: bool
    star: bool
    finid: int
    email: str
    phone: str
    comment: str
    auth: WdToken = None

class UnauthorizedError(BaseException):
    def __str__(self) -> str:
        return 'Wrong username or password :/'

class UnknownError(BaseException):
    pass

async def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

async def login_user(album: str, password: str) -> WdToken:
    _hash = await hash_password(password)
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

async def get_user_data(wdauth: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://wdauth.wsi.edu.pl/user?wdauth={wdauth}') as resp:
            user_data = await resp.json()
            return User(name=user_data['imie'], 
                        surname=user_data['nazwisko'], 
                        created_at=user_data['datarejestracji'], 
                        active=user_data['active'], 
                        star=user_data['star'], 
                        finid=user_data['finid'], 
                        email=user_data['email'], 
                        phone=user_data['phone'], 
                        comment=user_data['comment'])

async def main():
    load_dotenv()
    correct_password = os.getenv('correct_password')
    incorrect_password = os.getenv('incorrect_password')
    
    try:
        auth = await login_user('U/11', correct_password)

        user = await get_user_data(auth.wdauth)
        user.auth = auth
        print(user)
    except UnauthorizedError as e:
        print(str(e))

asyncio.run(main())
