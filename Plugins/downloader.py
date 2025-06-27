from pyrogram import filters
from youtube_dl import YoutubeDL
from ..main import app

ydl_opts = {"outtmpl": "%(title)s.%(ext)s"}

@app.on_message(filters.command(["yt", "ytmp3"]) & filters.me)
async def downloader_handler(c, m):
    link = m.text.split(maxsplit=1)[1]
    is_audio = m.text.startswith("/ytmp3")
    await m.reply("Processing...")
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        filename = ydl.prepare_filename(info)
    if is_audio:
        filename = filename.rsplit(".", 1)[0] + ".mp3"
    await m.reply_document(filename)
