from pyrogram import Client as app
from pyrogram import enums
from database import database
from config import *
import json
from bots.reply.start_text import *
@app.on_callback_query()
async def callback_query(client,callback_query):
    with open("bots/reply/text.json","r",encoding="UTF-8") as data:
        text = json.load(data)["lang_response"]
    data = callback_query.data
    if data[3:] in ["Amharic","English"]:
        user_id = callback_query.from_user.id
        first_name = callback_query.from_user.first_name
        database.edit_language(user_id,data[3:])
        if data[:2] == "st":
            await callback_query.edit_message_text(str(eval(data[3:])).format(first_name,user_id,user_id,admin_id),parse_mode=enums.ParseMode.MARKDOWN,disable_web_page_preview=True)
        else:
            await callback_query.edit_message_text(text[data[3:]])