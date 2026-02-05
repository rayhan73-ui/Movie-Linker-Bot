from pyrogram import Client, filters
from vars import Var

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def stream_handler(client, message):
    # মিডিয়া টাইপ চেক করা
    media = message.document or message.video or message.audio
    file_name = "Video_File"
    
    if media and hasattr(media, 'file_name') and media.file_name:
        file_name = media.file_name

    stream_link = f"{Var.URL}watch/{message.id}"
    download_link = f"{Var.URL}dl/{message.id}"

    await message.reply_text(
        f"**আপনার লিঙ্ক তৈরি হয়ে গেছে!** 🚀\n\n"
        f"📂 **ফাইলের নাম:** `{file_name}`\n"
        f"🔗 **স্ট্রিমিং লিঙ্ক:** {stream_link}\n"
        f"📥 **ডাউনলোড লিঙ্ক:** {download_link}",
        quote=True
    )
