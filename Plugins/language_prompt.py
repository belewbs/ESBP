from pyrogram import Client as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database import database
import json
from pyrogram import filters
from bots.filter.lang_filter import *

@app.on_message(lang_filter)
async def enforce(client,message):
    with open("bots/reply/text.json","r",encoding="UTF-8") as data:
        data = json.load(data)
    text = data["language_prompt"]
    await message.reply(text,reply_markup=InlineKeyboardMarkup(
                                                [[
                                                    InlineKeyboardButton("አማርኛ 🇪🇹",callback_data="st_Amharic"),
                                                    InlineKeyboardButton("English 🏴󠁧󠁢󠁥󠁮󠁧󠁿",callback_data="st_English")
                                                ]] ))