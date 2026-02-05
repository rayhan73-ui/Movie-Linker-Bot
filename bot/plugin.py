from pyrogram import Client, filters
import os

# এই ভেরিয়েবলগুলো রেন্ডারের ড্যাশবোর্ড থেকে সেট করবেন
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = os.environ.get("APP_URL") # আপনার রেন্ডার অ্যাপের লিঙ্ক

bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.video | filters.document)
async def generate_link(client, message):
    file_id = message.video.file_id if message.video else message.document.file_id
    # স্ট্রিম লিংক তৈরি (এটি একটি উদাহরণ, আপনার স্ট্রিমিং সার্ভারের লজিক অনুযায়ী হবে)
    stream_link = f"{APP_URL}/watch/{file_id}"
    
    await message.reply_text(f"✅ **আপনার স্ট্রিম লিংক তৈরি:**\n\n`{stream_link}`")

