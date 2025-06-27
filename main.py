import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Env vars
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# 👉 Plugin system use karo
app = Client(
    "KhatarnaakBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="plugins")  # 👈 important line
)

# 🎛️ Menu command
@app.on_message(filters.command("menu") & filters.me)
async def menu(c, m):
    from plugins.fonts import menu_markup  # 👈 just for this menu
    await m.reply(
        "⚙️ KhatarnaakBot Menu:",
        reply_markup=menu_markup
    )

# ▶️ Start
app.run()
