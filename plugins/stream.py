import os
import mimetypes
from flask import Flask, request, Response
from bot.bot_file import app as bot_app # আপনার বট অ্যাপ

server = Flask(__name__)

@server.route('/watch/<file_id>')
async def stream_video(file_id):
    # টেলিগ্রাম থেকে ফাইলটি স্ট্রিম করার লজিক
    try:
        # ফাইল ইনফো সংগ্রহ
        file_info = await bot_app.get_messages(None, file_id) # অথবা নির্দিষ্ট মেথড
        
        def generate():
            # এটি ভিডিওটিকে ছোট ছোট প্যাকেটে (Chunks) ভাগ করে ইউজারকে পাঠাবে
            for chunk in bot_app.stream_media(file_id):
                yield chunk

        # ভিডিওর টাইপ চেনা (যেমন mp4)
        mime_type = mimetypes.guess_type(request.args.get('name', 'video.mp4'))[0]
        
        return Response(generate(), mimetype=mime_type)
    except Exception as e:
        return str(e), 500

@server.route('/')
def health():
    return "Streaming Server is Active!"
