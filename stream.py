from flask import Flask, Response, request
from bot.bot_file import app as bot_app
import mimetypes

server = Flask(__name__)

@server.route('/')
def home():
    return "Streaming Server is Live! 🚀"

@server.route('/watch/<file_id>')
async def stream_video(file_id):
    try:
        # ফাইলটি সরাসরি টেলিগ্রাম থেকে স্ট্রিম করার জন্য মেথড
        async def generate():
            async for chunk in bot_app.stream_media(file_id):
                yield chunk

        # ভিডিওর নাম এবং টাইপ সেট করা
        file_name = request.args.get('name', 'video.mp4')
        mime_type, _ = mimetypes.guess_type(file_name)
        if not mime_type:
            mime_type = 'video/mp4'

        return Response(
            generate(),
            mimetype=mime_type,
            headers={
                "Content-Disposition": f"inline; filename={file_name}",
                "Accept-Ranges": "bytes"
            }
        )
    except Exception as e:
        print(f"Streaming error: {e}")
        return "Error: Could not stream the file.", 500
