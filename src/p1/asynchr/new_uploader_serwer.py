from asyncio import sleep
from random import randint
from urllib import request

from aiohttp import web
from aiohttp.abc import BaseRequest
from faker import Faker
import os
from os import path

routes = web.RouteTableDef()

# pip install aiohttp

"""
query = req.match_info.get('query', '')  # for route-resolving, /{query}
query = req.rel_url.query['query']  # params; required; else .get('query','default')
"""

def is_safe_path(basedir, path):
    return basedir == os.path.commonpath((basedir, os.path.abspath(path)))


@routes.get('/')
async def hello(request):
    print('request received')
    return web.json_response({'comment': f'hello, x={12}!'})


@routes.get('/welcome')
async def welcome(request):
    name = request.rel_url.query['name']
    await sleep(1.2)
    print(f'welcome request received for {name}')
    return web.json_response({'comment': f'hello {name}!'})


@routes.get('/users/{userid}/details')
async def welcome(request):
    # http://0.0.0.0:8888/users/i8811/details
    userid = request.match_info.get('userid', '')
    fake = Faker()
    user_name = fake.name()
    user_address = fake.address().replace('\n',', ')
    resp = {'userid': userid, 'name': user_name, 'address': user_address}
    return web.json_response(resp)


@routes.get('/serve/{filename}')
async def serve_file(req):
    filename = req.match_info.get('filename', '')
    if is_safe_path(os.getcwd(), filename):
        file_path = f'images/{filename}'
        if not path.exists(file_path):
            return web.HTTPNotFound()
        return web.FileResponse(file_path)
    return web.HTTPBadRequest()

@routes.post('/upload')
async def accept_file(req: BaseRequest):
    """
    Funkcja przyjmująca upload pliku.
    """
    # https://docs.aiohttp.org/en/stable/web_quickstart.html#file-uploads
    print('file upload request hit...')
    reader = await req.multipart()

    # field = await reader.next()
    # name = await field.read(decode=True)

    field = await reader.next()
    assert field.name == 'file'
    print(f'read field object: {field}')
    filename = field.filename
    # Cannot rely on Content-Length if transfer is chunked.
    print(f'filename:{filename}')
    filename = 'images/' + filename
    size = 0
    with open(filename, 'wb') as f:
        file_as_bytes = b''
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            print(type(chunk))
            if not chunk:
                break
            size += len(chunk)
            file_as_bytes += chunk
            # f.write(chunk)
        f.write(file_as_bytes)

    return web.json_response({'name': filename, 'size': size})



async def starter():
    """
    Starter / app factory, czyli miejsce gdzie można inicjalizować asynchronicze konstrukty.
    """
    await sleep(0.2)
    print('app is starting..')
    # await database.connect()
    return app


app = web.Application()
app.add_routes(routes)
web.run_app(starter(), port=8888)  # ewentu
