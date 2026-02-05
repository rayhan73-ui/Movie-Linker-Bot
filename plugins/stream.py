from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from vars import Var

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def stream_handler(client, message: Message):
    # ফাইল আইডি তৈরি করা
    file_id = message.document.file_id if message.document else (message.video.file_id if message.video else message.audio.file_id)
    file_name = message.document.file_name if message.document else (message.video.file_name if message.video else "audio_file")
    
    # লিঙ্ক তৈরি (vars.py এর URL লজিক ব্যবহার করে)
    # এখানে আমরা একটি ইউনিক আইডি হিসেবে মেসেজ আইডি ব্যবহার করছি (সহজ করার জন্য)
    stream_link = f"{Var.URL}watch/{message.id}"
    download_link = f"{Var.URL}dl/{message.id}"

    text = (
        f"**আপনার লিঙ্ক তৈরি হয়ে গেছে!** 🚀\n\n"
        f"📂 **ফাইলের নাম:** `{file_name}`\n"
        f"🔗 **স্ট্রিমিং লিঙ্ক:** {stream_link}\n"
        f"📥 **ডাউনলোড লিঙ্ক:** {download_link}"
    )

    await message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🚀 Stream Now", url=stream_link),
              InlineKeyboardButton("📥 Download", url=download_link)]]
        ),
        quote=True
                                                                )
