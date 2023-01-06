from pyrogram import Client
from config import *

Client("esbp",
api_id=api_id,api_hash=api_hash,bot_token=bot_token,
plugins={
    "root" : "Plugins",
    "include" : ["language_prompt","callback_query","start","status","change_language","message_handler","userstatus"]
}
).run()