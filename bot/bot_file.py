from pyrogram import Client, filters
import os

# আপনার তথ্যগুলো এখানে দিন (অথবা Render Environment Variables এ যোগ করুন)
API_ID = int(os.environ.get("API_ID", "12345")) # আপনার API ID
API_HASH = os.environ.get("API_HASH", "your_api_hash") # আপনার API Hash
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token") # আপনার Bot Token
APP_URL = os.environ.get("APP_URL", "") # আপনার Render অ্যাপের URL (e.g. https://my-bot.onrender.com)

app = Client(
    "stream_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.video | filters.document | filters.audio)
async def gen_link(client, message):
    if not APP_URL:
        await message.reply_text("❌ দয়া করে Render-এ `APP_URL` এনভায়রনমেন্ট ভেরিয়েবলটি সেট করুন।")
        return

    # ফাইলের তথ্য সংগ্রহ
    file = message.video or message.document or message.audio
    file_id = file.file_id
    file_name = getattr(file, 'file_name', 'video.mp4')
    
    # স্ট্রিম লিংক তৈরি
    # নোট: এটি একটি ডাইনামিক লিংক যা আপনার সার্ভারের মাধ্যমে প্রসেস হবে
    stream_link = f"{APP_URL}/watch/{file_id}?name={file_name.replace(' ', '%20')}"
    download_link = f"{APP_URL}/download/{file_id}?name={file_name.replace(' ', '%20')}"

    text = (
        f"✅ **আপনার ফাইলটি রেডি!**\n\n"
        f"📄 **ফাইলের নাম:** `{file_name}`\n\n"
        f"🔗 **সরাসরি স্ট্রিম লিংক:**\n`{stream_link}`\n\n"
        f"📥 **সরাসরি ডাউনলোড লিংক:**\n`{download_link}`\n\n"
        f"💡 *টিপস: এই লিংকটি VLC বা অন্য যেকোনো প্লেয়ারে কাজ করবে।*"
    )
    
    await message.reply_text(text, disable_web_page_preview=True)

