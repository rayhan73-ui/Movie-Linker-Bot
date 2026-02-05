from aiohttp import web

async def dl_handler(request):
    # এই অংশটি লিঙ্কে ক্লিক করলে রেসপন্স দেবে
    return web.Response(text="সার্ভার সচল আছে! আপনার ফাইলটি স্ট্রিম হওয়ার জন্য প্রস্তুত।", content_type='text/html')

async def web_server():
    app = web.Application()
    app.add_routes([
        web.get('/dl/{id}', dl_handler),
        web.get('/watch/{id}', dl_handler),
        web.get('/', dl_handler)
    ])
    return app
