import gevent.monkey
gevent.monkey.patch_all() # gevent এর জন্য এটি সবার আগে থাকতে হবে

import os
import asyncio
from gevent.pywsgi import WSGIServer
from stream import server as flask_app # stream.py থেকে ফ্ল্যাস্ক অ্যাপ আনা
from bot.bot_file import app as bot_app # bot/bot_file.py থেকে বট আনা

async def start_bot():
    """টেলিগ্রাম বট চালু করার ফাংশন"""
    try:
        await bot_app.start()
        print("✅ Telegram Bot started successfully!")
    except Exception as e:
        print(f"❌ Error starting bot: {e}")

def run_server():
    """ফ্ল্যাস্ক স্ট্রিমিং সার্ভার চালু করার ফাংশন"""
    port = int(os.environ.get("PORT", 8080))
    print(f"🚀 Streaming Server running on port {port}...")
    http_server = WSGIServer(('0.0.0.0', port), flask_app)
    http_server.serve_forever()

async def main():
    # প্রথমে বট স্টার্ট হবে
    await start_bot()
    
    # তারপর সার্ভার এবং বটের ইভেন্ট লুপ একসাথে চলবে
    # রেন্ডার সার্ভার চালু রাখার জন্য run_server কল করা হলো
    gevent.spawn(run_server)
    
    # বটকে আজীবন চালু রাখার জন্য
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Stopping...")
