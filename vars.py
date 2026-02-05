# This file is a part of FileStreamBot
from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID"))
    API_HASH = str(environ.get("API_HASH"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN"))
    BIN_CHANNEL = int(environ.get("BIN_CHANNEL"))
    DATABASE_URL = str(environ.get('DATABASE_URL'))
    OWNER_ID = int(environ.get('OWNER_ID'))
    
    # Render Settings
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
    
    # FQDN Logic for Render
    FQDN = str(environ.get("FQDN", BIND_ADDRESS)).replace("https://", "").replace("http://", "").strip("/")
    
    # URL Logic
    if "onrender.com" in FQDN:
        URL = f"https://{FQDN}/"
    else:
        URL = f"http://{FQDN}:{PORT}/"

    UPDATES_CHANNEL = str(environ.get('UPDATES_CHANNEL', "Telegram"))
    SESSION_NAME = str(environ.get('SESSION_NAME', 'FileStreamBot'))
    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "1")).lower() in ("1", "true", "yes")
