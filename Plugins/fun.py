import random
from pyrogram import filters
from ..main import app

@ app.on_message(filters.command(["joke", "truth", "dare", "fact"]) & filters.me)
async def fun_handler(c, m):
    cmd = m.command[0]
    samples = {
        "joke": ["Joke 1", "Joke 2"],
        "truth": ["Truth 1", "Truth 2"],
        "dare": ["Dare 1", "Dare 2"],
        "fact": ["Fact 1", "Fact 2"],
    }
    await m.reply(random.choice(samples[cmd]))
