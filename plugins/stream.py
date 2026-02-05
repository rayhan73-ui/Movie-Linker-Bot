from pyrogram import Client, filters
from vars import Var

@Client.on_message(filters.private & (filters.document | filters.video))
async def stream_handler(client, message):
    media = message.document or message.video
    file_name = getattr(media, 'file_name', "Video_File.mp4")

    try:
        log_msg = await message.forward(chat_id=Var.BIN_CHANNEL)
    except Exception as e:
        await message.reply_text(f"Error: {e}")
        return

    stream_link = f"{Var.URL}watch/{log_msg.id}"
    download_link = f"{Var.URL}dl/{log_msg.id}"

    await message.reply_text(
        f"**লিঙ্ক তৈরি হয়ে গেছে!** 🚀\n\n"
        f"📂 **ফাইলের নাম:** `{file_name}`\n"
        f"🔗 **স্ট্রিমিং লিঙ্ক:** {stream_link}\n"
        f"📥 **ডাউনলোড লিঙ্ক:** {download_link}",
        quote=True
    )
