from server import start_server
from bot.plugin import bot
import asyncio

if __name__ == "__main__":
    start_server() # ওয়েব সার্ভার চালু করবে
    print("বট চালু হচ্ছে...")
    bot.run() # টেলিগ্রাম বট চালু করবে
