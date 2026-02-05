from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from vars import Var

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        text=f"হ্যালো {message.from_user.mention},\n\nআমি একটি ফাইল স্ট্রীম বট। আমাকে যেকোনো ফাইল বা ভিডিও পাঠান, আমি আপনাকে সরাসরি ডাউনলোড এবং স্ট্রীমিং লিঙ্ক দেব।",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")]]
        )
    )
