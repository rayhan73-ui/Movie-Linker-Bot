import logging
import asyncio
from pyrogram import Client
from vars import Var
from utils.keepalive import start_server

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
        # ওয়েব সার্ভার শুরু করা যা Render এর পোর্ট এরর ঠিক করবে
        await start_server()
        me = await self.get_me()
        print(f"--- {me.first_name} Started Successfully ---")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
