import asyncio
from aiohttp import web
from vars import Var

async def status_handler(request):
    return web.Response(text="Bot is running smoothly!")

async def start_server():
    app = web.Application()
    app.add_routes([web.get('/', status_handler)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, Var.BIND_ADDRESS, Var.PORT)
    await site.start()
