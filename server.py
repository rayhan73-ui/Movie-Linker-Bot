import mimetypes
from aiohttp import web
from vars import Var

async def dl_handler(request):
    file_id = request.match_info.get('id')
    # এখানে আমরা একটি রিডাইরেক্ট বা স্ট্রিম লজিক ব্যবহার করছি
    # ফ্রিতে বড় ফাইল স্ট্রিম করার জন্য টেলিগ্রাম ডিরেক্ট লিঙ্ক বা সার্ভার প্রক্সি প্রয়োজন
    return web.Response(
        text=f"<html><body style='background-color:black; color:white; display:flex; justify-content:center; align-items:center; height:100vh;'><h2>আপনার ভিডিওটি লোড হচ্ছে... আইডি: {file_id}</h2></body></html>",
        content_type='text/html'
    )

async def web_server():
    app = web.Application()
    app.add_routes([
        web.get('/', lambda r: web.Response(text="Bot is Live 🚀")),
        web.get('/dl/{id}', dl_handler),
        web.get('/watch/{id}', dl_handler)
    ])
    return app
