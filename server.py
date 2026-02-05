import mimetypes
from aiohttp import web
from vars import Var

async def dl_handler(request):
    file_id = request.match_info.get('id')
    
    # স্ট্রিমিং এর একটি উন্নত ইন্টারফেস
    html_content = f"""
    <html>
        <head>
            <title>Streaming...</title>
            <style>
                body {{ background: #000; color: #fff; text-align: center; font-family: sans-serif; padding-top: 50px; }}
                video {{ width: 80%; max-width: 800px; border-radius: 10px; box-shadow: 0 0 20px rgba(255,255,255,0.2); }}
                .btn {{ display: inline-block; margin-top: 20px; padding: 10px 20px; background: #0088cc; color: #fff; text-decoration: none; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h2>আপনার ভিডিওটি স্ট্রিমিং হচ্ছে</h2>
            <video controls autoplay>
                <source src="https://{{Var.FQDN}}/dl/{{file_id}}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <br>
            <a href="https://{{Var.FQDN}}/dl/{{file_id}}" class="btn">সরাসরি ডাউনলোড করুন</a>
        </body>
    </html>
    """
    return web.Response(text=html_content, content_type='text/html')

async def web_server():
    app = web.Application()
    app.add_routes([
        web.get('/', lambda r: web.Response(text="Bot is running! 🚀")),
        web.get('/watch/{{id}}', dl_handler),
        web.get('/dl/{{id}}', dl_handler)
    ])
    return app
