import os

API_ID    = os.environ.get("API_ID", "24037760")
API_HASH  = os.environ.get("API_HASH", "dccc3070f1c12ab155011f14c3d6ae6a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
