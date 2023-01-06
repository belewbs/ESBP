from pyrogram import Client as app
from pyrogram import filters
from database import database
import json

@app.on_message(filters.command("status"))
async def status(client,message):
    with open("bots/reply/text.json","r",encoding="UTF-8") as d:
        text_lang = json.load(d)["status"]
    user_id = message.chat.id
    language = database.get_user(user_id)["language"]
    members = database.active_member()
    await message.reply(text_lang[language].format(members))