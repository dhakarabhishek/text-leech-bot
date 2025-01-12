import os

API_ID    = os.environ.get("API_ID", "22551612")
API_HASH  = os.environ.get("API_HASH", "3936fa8e723ae5777300b8245118920b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
