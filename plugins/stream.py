from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from vars import Var
import math

def humanbytes(size):
    if not size: return "0 B"
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024: return f"{size:.2f} {unit}"
        size /= 1024

@Client.on_message(filters.private & (filters.document | filters.video))
async def stream_handler(client, message):
    media = message.document or message.video
    file_name = getattr(media, 'file_name', "video-file.mp4")
    file_size = humanbytes(media.file_size)

    # স্টোরেজ চ্যানেলে পাঠানো
    log_msg = await message.forward(chat_id=Var.BIN_CHANNEL)
    
    stream_link = f"{Var.URL}watch/{log_msg.id}"
    download_link = f"{Var.URL}dl/{log_msg.id}"

    text = (
        f"✨ **Your Link Generated !**\n\n"
        f"📂 **FILE NAME :**\n`{file_name}`\n\n"
        f"📦 **FILE SIZE :** `{file_size}`\n\n"
        f"📥 **DOWNLOAD :** {download_link}\n\n"
        f"🖥️ **WATCH :** {stream_link}"
    )

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🖥️ STREAM", url=stream_link),
         InlineKeyboardButton("📥 DOWNLOAD", url=download_link)]
    ])

    await message.reply_text(text=text, reply_markup=reply_markup, quote=True)
