import asyncio
from stream import server
from bot.bot_file import app as bot_app
import os

async def main():
    # বট স্টার্ট করা
    await bot_app.start()
    print("Bot is started!")
    
    # সার্ভার রান করা (রেন্ডারের জন্য)
    port = int(os.environ.get("PORT", 8080))
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('0.0.0.0', port), server)
    http_server.serve_forever()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
