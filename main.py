import logging
from pyrogram import Client
from vars import Var
from server import web_server
from aiohttp import web

logging.basicConfig(level=logging.INFO)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=Var.SESSION_NAME,
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            bot_token=Var.BOT_TOKEN,
            plugins={'root': 'plugins'}
        )

    async def start(self):
        await super().start()
        # ওয়েব সার্ভার চালু করা
        app = await web_server()
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, Var.BIND_ADDRESS, Var.PORT)
        await site.start()
        print("--- Bot & Server Started Successfully ---")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
