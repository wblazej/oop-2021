from asyncio import sleep

from aiohttp import web
from os import uname
from is_prime import is_prime

routes = web.RouteTableDef()

# aiohttp ... (pip install aiohttp)
"""
query = req.match_info.get('query', '')  # for route-resolving, /{query}
query = req.rel_url.query['query']  # params; required; else .get('query','default')
"""


@routes.get('/')
async def hello(request):
    n = uname()
    print(f'{n.nodename} request received')
    return web.json_response({'comment': f'hello from {n.nodename}!'})


@routes.get('/welcome')
async def hello(request):
    name = request.rel_url.query['name']
    await sleep(1.2)
    print(f'welcome request received for {name}')
    return web.json_response({'comment': f'hello {name}!'})


@routes.get('/add')
async def hello(request):
    a = float(request.rel_url.query['a'])
    b = float(request.rel_url.query['b'])
    return web.json_response({'result': a + b})

@routes.get('/is_prime')
async def is_prime_(request):
    x = float(request.rel_url.query['x'])
    return web.json_response({'result': await is_prime(x)})


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=4411)