from random import randint

from aiohttp import web

routes = web.RouteTableDef()

# pip install aiohttp

async def get_x():
    return randint(0,100)

@routes.get('/')
async def hello(request):
    print('request received')
    x = await get_x()
    return web.json_response({'comment': f'hello, x={x}!'})


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8888)  # ewentu
