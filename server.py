import mimetypes
from aiohttp import web
from vars import Var
from bot import Bot # আপনার বটের মেইন ফাইল থেকে ক্লায়েন্ট ইম্পোর্ট

async def dl_handler(request):
    file_id = int(request.match_info.get('id'))
    
    # আপনার স্টোরেজ চ্যানেল থেকে মেসেজটি খুঁজে বের করা
    try:
        msg = await Bot.get_messages(Var.BIN_CHANNEL, file_id)
        media = msg.document or msg.video
        
        # এখানে ফাইলটিকে স্ট্রিম করার জন্য টেলিগ্রাম সার্ভারে রিকোয়েস্ট পাঠানো হয়
        # এই অংশটিই লিঙ্কটিকে "ওয়ার্কিং" বানায়
        response = web.StreamResponse()
        response.content_type = media.mime_type or 'video/mp4'
        
        await response.prepare(request)
        
        # ফাইলটি চাঙ্ক (Chunk) আকারে ব্রাউজারে পাঠানো
        async for chunk in Bot.stream_media(media):
            await response.write(chunk)
            
        return response
    except Exception as e:
        return web.Response(text=f"Error: {e}", status=500)

async def web_server():
    app = web.Application()
    app.add_routes([
        web.get('/', lambda r: web.Response(text="Server is Online! 🚀")),
        web.get('/dl/{id}', dl_handler),
        web.get('/watch/{id}', dl_handler)
    ])
    return app
