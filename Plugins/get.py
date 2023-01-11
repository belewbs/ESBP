from pyrogram import Client as app
from pyrogram import filters
import json
from database import database
from bots.button.get_btn import *
with open("bots/reply/text.json","r",encoding="UTF-8") as texts:
    text = json.load(texts)["get_grade"]
@app.on_message(filters.command("get"))
async def get(client,message):
    user_id = message.chat.id
    language = database.get_user(user_id)["language"]
    await message.reply(text[language],reply_markup=grade)