from pyrogram import filters
from ..main import app

@ app.on_message(filters.command(["ban", "mute", "kick", "del"]) & filters.me)
async def admin_handler(c, m):
    cmd = m.command[0]
    if cmd in ["ban", "kick", "mute"]:
        target = m.reply_to_message.from_user.id
        if cmd == "ban":
            await c.ban_chat_member(m.chat.id, target)
        elif cmd == "kick":
            await c.kick_chat_member(m.chat.id, target)
    else:
        await m.reply_to_message.delete()
