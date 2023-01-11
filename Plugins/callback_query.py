from pyrogram import Client as app
from pyrogram import enums
from pyrogram.types import ForceReply
from database import database
from config import *
import json
from bots.button.get_btn import *
from bots.reply.start_text import *
@app.on_callback_query()
async def callback_query(client,callback_query):
    subjects = ["amharic","english","math","physics","biology","chemistry","history","geography","economics","ict","civics","business"]
    data = callback_query.data
    if data[3:] in ["Amharic","English"]:
        with open("bots/reply/text.json","r",encoding="UTF-8") as d:
            text = json.load(d)["lang_response"]
        user_id = callback_query.from_user.id
        first_name = callback_query.from_user.first_name
        database.edit_language(user_id,data[3:])
        if data[:2] == "st":
            await callback_query.edit_message_text(str(eval(data[3:])).format(first_name,user_id,user_id,admin_id),parse_mode=enums.ParseMode.MARKDOWN,disable_web_page_preview=True)
        else:
            await callback_query.edit_message_text(text[data[3:]])
    elif data in ["9","10","11","12"]:
        grade_btn  = f"sub_{data}"
        with open("bots/reply/text.json","r",encoding="UTF-8") as d:
            text = json.load(d)
        user_id = callback_query.from_user.id
        language = database.get_user(user_id)["language"]
        subject_choose = text["get_sub"][language]
        database.add_message(callback_query.message.id,{"grade":data,"subject":None})
        await callback_query.edit_message_text(subject_choose,reply_markup=eval(grade_btn))
    elif data == "back":
        with open("bots/reply/text.json","r",encoding="UTF-8") as texts:
            text = json.load(texts)["get_grade"]
        user_id = callback_query.from_user.id
        language = database.get_user(user_id)["language"]
        await callback_query.edit_message_text(text[language],reply_markup=grade)
    elif data in subjects:
        with open("bots/reply/text.json","r",encoding="UTF-8") as d:
            text = json.load(d)
        user_id = callback_query.from_user.id
        language = database.get_user(user_id)["language"]
        page_text = text["get_page"][language]
        holder_text = text["get_page_holder"][language]
        grade_data = database.message_status(callback_query.message.id)["data"]["grade"]
        database.update_message(callback_query.message.id,{"grade":grade_data,"subject":data[:2]})
        await client.send_message(user_id,page_text,reply_markup=ForceReply(selective=False,placeholder=holder_text))