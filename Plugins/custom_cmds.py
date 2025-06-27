from pyrogram import filters
from ..main import app
import pyautogui

@app.on_message(filters.command("ss") & filters.me)
async def ss_handler(c, m):
    path = "ss.png"
    img = pyautogui.screenshot(path)
    await m.reply_photo(path)
