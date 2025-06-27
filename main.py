import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Environment variables se read karo
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client("KhatarnaakBot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)


# Register plugin handlers
app.add_handler(fonts.fonts_handler)
app.add_handler(downloader.downloader_handler)
app.add_handler(fun.fun_handler)
app.add_handler(admin_tools.admin_handler)
app.add_handler(screenshot.ss_handler)
app.add_handler(recorder.rec_handler)
app.add_handler(custom_cmds.custom_handler)

# Menu command
@app.on_message(filters.command("menu") & filters.me)
async def menu(c, m):
    await m.reply(
        "⚙️ KhatarnaakBot Menu:",
        reply_markup=fonts.menu_markup
    )

app.run()
