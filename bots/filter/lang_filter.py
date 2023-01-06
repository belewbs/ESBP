from database import database
from pyrogram import filters

def language_filter(_,__,message):
    user_id = message.chat.id
    user = database.get_user(user_id)
    if user == None:
        first_name = message.from_user.first_name
        database.append_user(user_id,first_name)
        return True
    elif user["language"] == "undefine":
        return True
    return False
lang_filter = filters.create(language_filter)