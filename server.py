from aiohttp import web
from vars import Var

async def dl_handler(request):
    return web.Response(text="ফাইল ডাউনলোড সিস্টেম শীঘ্রই আসছে। আপনার সার্ভার সঠিকভাবে রান করছে!")

async def web_server():
    app = web.Application()
    app.add_routes([
        web.get('/dl/{id}', dl_handler),
        web.get('/watch/{id}', dl_handler)
    ])
    return app

# এটি Render এর পোর্টে সার্ভার রান করাবে
if __name__ == "__main__":
    app = web_server()
    web.run_app(app, port=Var.PORT)
