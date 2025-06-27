from pyrogram import filters
from ..main import app
import subprocess

@app.on_message(filters.command("rec") & filters.me)
async def rec_handler(c, m):
    out = "rec.mp4"
    subprocess.run(["ffmpeg", "-video_size", "1920x1080", "-framerate", "15", "-f", "x11grab", "-i", ":0.0", out])
    await m.reply_document(out)
