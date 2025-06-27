from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ..main import app

font_commands = ["danger", "ghost", "devil", "love", "khatarnaak", "sadboy", "swag", "cursed", "aesthetic"]

menu_markup = InlineKeyboardMarkup(
    [[InlineKeyboardButton(cmd, callback_data=f"font_{cmd}") for cmd in font_commands[:3]],
     [InlineKeyboardButton(cmd, callback_data=f"font_{cmd}") for cmd in font_commands[3:6]],
     [InlineKeyboardButton("← Back", callback_data="menu")]]
)

@app.on_callback_query(filters.regex(r"^font_"))
async def font_cb(c, cb):
    cmd = cb.data.split("_", 1)[1]
    await cb.message.edit(f"<b>{cmd.upper()}</b>", reply_markup=None)

@app.on_message(filters.command(font_commands) & filters.me)
async def fonts_handler(c, m):
    cmd = m.text.split()[0][1:]
    await m.reply(f"<i>{cmd.upper()}</i>")
