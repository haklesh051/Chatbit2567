import time
import asyncio
asyncio.get_event_loop().time = time.time  # 👈 ये लाइन डालना ज़रूरी है

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client(
    "KhatarnaakBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="plugins")
)

@app.on_message(filters.command("menu") & filters.me)
async def menu(c, m):
    from plugins.fonts import menu_markup
    await m.reply("⚙️ KhatarnaakBot Menu:", reply_markup=menu_markup)

app.run()
