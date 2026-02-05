from pyrogram import Client, filters
from vars import Var

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def stream_handler(client, message):
    # ভিডিও বা ডকুমেন্টের তথ্য সংগ্রহ
    media = message.document or message.video or message.audio
    file_name = "Video_File.mp4" # ডিফল্ট নাম
    
    if media and hasattr(media, 'file_name') and media.file_name:
        file_name = media.file_name

    # লিঙ্ক জেনারেশন
    stream_link = f"{Var.URL}watch/{message.id}"
    download_link = f"{Var.URL}dl/{message.id}"

    text = (
        f"**আপনার লিঙ্ক তৈরি হয়ে গেছে!** 🚀\n\n"
        f"📂 **ফাইলের নাম:** `{file_name}`\n"
        f"🔗 **স্ট্রিমিং লিঙ্ক:** {stream_link}\n"
        f"📥 **ডাউনলোড লিঙ্ক:** {download_link}"
    )

    await message.reply_text(text=text, quote=True)
