import mimetypes
from aiohttp import web
from vars import Var

async def dl_handler(request):
    file_id = request.match_info.get('id')
    
    # স্ট্রিমিং প্লেয়ার ইন্টারফেস
    html_content = f"""
    <html>
        <head>
            <title>Streaming Video</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ background: #000; color: #fff; text-align: center; font-family: sans-serif; margin: 0; padding: 20px; }}
                video {{ width: 100%; max-width: 700px; border-radius: 8px; background: #222; }}
                .container {{ margin-top: 50px; }}
                .download-btn {{ display: inline-block; margin-top: 25px; padding: 12px 25px; background: #0088cc; color: white; text-decoration: none; border-radius: 50px; font-weight: bold; transition: 0.3s; }}
                .download-btn:hover {{ background: #006699; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>আপনার ভিডিওটি প্লে হচ্ছে</h2>
                <video controls autoplay>
                    <source src="/dl/{file_id}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <br>
                <a href="/dl/{file_id}" class="download-btn">সরাসরি ডাউনলোড করুন (Fast)</a>
            </div>
        </body>
    </html>
    """
    return web.Response(text=html_content, content_type='text/html')

async def web_server():
    app = web.Application()
    app.add_routes([
        web.get('/', lambda r: web.Response(text="Bot is Live! 🚀")),
        web.get('/watch/{id}', dl_handler),
        web.get('/dl/{id}', dl_handler) # ডাউনলোড এবং স্ট্রিম পাথ একই রাখা হয়েছে
    ])
    return app
