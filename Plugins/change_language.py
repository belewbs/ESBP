from pyrogram import Client as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from database import database
import json
@app.on_message(filters.command("change_language"))
async def change_lang(client,message):
    with open("bots/reply/text.json","r",encoding="UTF-8") as data:
        data = json.load(data)
    text = data["language_prompt"]
    await message.reply(text,reply_markup=InlineKeyboardMarkup(
                                                [[
                                                    InlineKeyboardButton("አማርኛ 🇪🇹",callback_data="ch_Amharic"),
                                                    InlineKeyboardButton("English 🏴󠁧󠁢󠁥󠁮󠁧󠁿",callback_data="ch_English")
                                                ]] ))