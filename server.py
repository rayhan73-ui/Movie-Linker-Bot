from aiohttp import web
from vars import Var

async def dl_handler(request):
    file_id = request.match_info.get('id')
    
    html = f"""
    <html>
        <head>
            <title>Streaming...</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ background: #0e0e0e; color: white; font-family: 'Segoe UI', sans-serif; text-align: center; margin: 0; padding: 20px; }}
                .player-card {{ background: #1a1a1a; padding: 20px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); display: inline-block; width: 100%; max-width: 600px; }}
                video {{ width: 100%; border-radius: 10px; border: 1px solid #333; }}
                .btn {{ display: block; margin-top: 20px; padding: 15px; background: #0088cc; color: white; text-decoration: none; border-radius: 8px; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="player-card">
                <h3>🎬 Video Player</h3>
                <video controls autoplay>
                    <source src="https://{Var.FQDN}/dl/{file_id}" type="video/mp4">
                </video>
                <a href="https://{Var.FQDN}/dl/{file_id}" class="btn">📥 Fast Download</a>
            </div>
        </body>
    </html>
    """
    return web.Response(text=html, content_type='text/html')

async def web_server():
    app = web.Application()
    app.add_routes([
        web.get('/', lambda r: web.Response(text="Bot is Active!")),
        web.get('/watch/{{id}}', dl_handler),
        web.get('/dl/{{id}}', dl_handler)
    ])
    return app
