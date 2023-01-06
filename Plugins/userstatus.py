from pyrogram import Client as app
from pyrogram.raw import types
from database import database
@app.on_raw_update()    
async def raw(client, update, users, chats):
    if isinstance(update, types.UpdateBotStopped):
        user = users[update.user_id]
        if update.stopped:
            database.remove(user.id)
        else:
            database.append_user(user.id,user.first_name)