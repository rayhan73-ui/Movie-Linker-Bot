import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

from pyrogram import Client
from vars import Var
from aiohttp import web

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=Var.SESSION_NAME,
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            bot_token=Var.BOT_TOKEN,
            workers=20,
            plugins={'root': 'plugins'} # আমরা প্লাগইন সিস্টেম ব্যবহার করব
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"--- Bot Started: {me.first_name} ---")
        print(f"URL => {Var.URL}")

    async def stop(self, *args):
        await super().stop()
        print("--- Bot Stopped ---")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
