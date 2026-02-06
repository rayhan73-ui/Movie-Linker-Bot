from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = os.environ.get("APP_URL")

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# স্টার্ট কমান্ডের জন্য
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("বট চালু আছে! আমাকে ভিডিও পাঠান।")

# ভিডিও বা ফাইল পাঠালে লিংক দিবে
@app.on_message(filters.video | filters.document)
async def stream(client, message):
    file_id = message.video.file_id if message.video else message.document.file_id
    stream_link = f"{APP_URL}/watch/{file_id}"
    await message.reply_text(f"আপনার লিংক: {stream_link}")
