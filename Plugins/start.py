from pyrogram import filters,enums
from pyrogram import Client as app
from database import database
from config import *
from bots.reply.start_text import *
@app.on_message(filters.command("start"))
async def start(client,message):
    user_id = message.chat.id
    first_name = message.from_user.first_name
    language = database.get_user(user_id)["language"]
    await message.reply(text=str(eval(language)).format(first_name,user_id,admin_id),parse_mode=enums.ParseMode.MARKDOWN,disable_web_page_preview=True)
