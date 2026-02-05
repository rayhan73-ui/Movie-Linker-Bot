from pyrogram import Client, filters
from vars import Var

@Client.on_message(filters.private & (filters.document | filters.video))
async def stream_handler(client, message):
    media = message.document or message.video
    # আসল নাম রিড করার সঠিক পদ্ধতি
    file_name = getattr(media, 'file_name', "Video_File.mp4")
    
    # ফাইলটি স্টোরেজ চ্যানেলে পাঠানো
    log_msg = await message.forward(chat_id=Var.BIN_CHANNEL)
    
    # লিঙ্ক জেনারেট করা
    stream_link = f"{Var.URL}watch/{log_msg.id}"
    
    await message.reply_text(
        f"✅ **লিঙ্ক তৈরি হয়েছে!**\n\n📂 নাম: `{file_name}`\n🔗 লিঙ্ক: {stream_link}",
        quote=True
    )
