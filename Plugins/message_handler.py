from pyrogram import Client as app
from main import get_id,get_image
from pyrogram import filters,enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import enums
from database import database
from config import *
import json
@app.on_message(filters.text)
async def send_message(client,message):
    with open("bots/reply/text.json","r",encoding="UTF-8") as data:
            json_data = json.load(data)
    text = message.text.lower()
    user_id = message.chat.id
    users_id = database.users_id()
    first_name = message.from_user.first_name
    language = database.get_user(user_id)["language"]
    '''
    for feedback
    '''
    if message.text[:8] == "feedback":
        feedback_text = json_data["feedback"]
        reply_text = json_data["feedback_reply"][language]
        await message.reply(reply_text)
        await client.send_message(admin_id,feedback_text.format(first_name,user_id,user_id,message.text[8:]),parse_mode=enums.ParseMode.MARKDOWN)
        '''
    For send feedback response from the admin to the specific user
    format -> -f |txt=text|id=id
    '''
    elif text[:2].lower() == "-f" and user_id == admin_id:
        admin_reply = json_data["admin_reply"][language]
        to_admin = json_data["to_admin"]
        msg = text.split("|")
        id = False
        ad_msg = False
        for i in msg:
            if "id" in i:
                id = i[3:]
            if "txt" in i:
                ad_msg = i[4:]
        await client.send_message(int(id),admin_reply.format(first_name,user_id,ad_msg),parse_mode=enums.ParseMode.MARKDOWN)
        await message.reply(to_admin)
        '''
    for admin to send message to all users
    format -> -sm |text=text|img=url|btn=btn_name-btn_url|
              for trial use -sm preview |text=text|img=url|btn=btn_name-btn_url|
    '''
    elif text[:3].lower() == "-sm" and user_id == admin_id:
        msg = text.split("|")
        txt,img,btn,preview = [False for i in range(4)]
        for i in msg:
            if "preview" in i:
                preview = True
            if "txt" in i:
                txt = i[4:]
            if "img" in i:
                img = i[4:]
            if "btn" in i:
                btn = i[4:].split("-")
        users_id = [(admin_id)] if preview == True else users_id
        for user_id in users_id:
                if txt != False and img != False and btn != False:
                    await client.send_photo(int(user_id),photo=img,caption=txt,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(btn[0],url=btn[1])]] ),parse_mode=enums.ParseMode.MARKDOWN)
                elif btn == False and img == False:
                    await client.send_message(int(user_id),txt,parse_mode=enums.ParseMode.MARKDOWN)
                elif btn == False and txt == False:
                    await client.send_photo(int(user_id),img,parse_mode=enums.ParseMode.MARKDOWN)
                elif btn == False :
                    await client.send_photo(int(user_id),caption=txt,photo=img,parse_mode=enums.ParseMode.MARKDOWN)
                elif txt == False:
                    await client.send_photo(int(user_id),photo=img,parse_mode=enums.ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(btn[0],url=btn[1])]] )) 
                elif img == False:
                    await client.send_message(int(user_id),txt,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(btn[0],url=btn[1])]] ),parse_mode=enums.ParseMode.MARKDOWN)
#--------------------------------------------------------------------------------------
        """
    If the user wanna get the image using buttons
    """
    elif database.message_status(int(message.id)-2) != None:
        grade_data = database.message_status(message.id-2)["data"]["grade"]
        subject_data = database.message_status(message.id-2)["data"]["subject"]
        if "-" in message.text:
            if len(message.text.split("-")) == 2:
                intial,final = message.text.split("-")
                if (int(final)-int(intial))+1 <= 5:
                    for i in range(int(intial),int(final)+1):
                        id = get_id(subject_data,grade_data,i)
                        if id [0]== False:
                            await client.send_message(user_id,json_data["page_max"][language].format(id[1]))
                        elif id[0] == True:
                            image = get_image(id[1])
                            await client.send_photo(user_id,photo=image)
                    await client.send_message(user_id,json_data["done"][language])
                else:
                    await client.send_message(user_id,json_data["get_page_max"][language])
            else:
                await client.send_message(user_id,json_data["hyphen_error"][language])
        else:
            id = get_id(subject_data,grade_data,int(message.text))
            if id[0] == False:
                await client.send_message(user_id,json_data["page_max"][language].format(id[1]))
            else:
                image = get_image(id[1])
                await client.send_photo(chat_id=user_id,photo=image)
    else:
        splitted_text = text.split(",")
        if len(splitted_text) < 3 or len(splitted_text) > 3:
            await message.reply(json_data["warning"][language],parse_mode=enums.ParseMode.MARKDOWN)
        else:
            subject = splitted_text[0]
            grade = splitted_text[1]
            page = splitted_text[2]
            if "-" in page:
                if len(page.split("-")) == 2:
                    intial,final = page.split("-")
                    if (int(final)-int(intial))+1 <= 5:
                        for i in range(int(intial),int(final)+1):
                            id = get_id(subject[:2],grade,i)
                            if id[0] == False:
                                await client.send_message(user_id,json_data["page_max"][language].format(id[1]))
                            else:
                                image = get_image(id[1])
                                await client.send_photo(chat_id=user_id,photo=image)
                        await client.send_message(user_id,json_data["done"][language])
                    else:
                        await client.send_message(user_id,json_data["get_page_max"][language])
                else:
                    await client.send_message(user_id,json_data["hyphen_error"][language])
            else:
                id = get_id(subject[:2],grade,int(page))
                if id[0] == False:
                    await client.send_message(user_id,json_data["page_max"][language].format(id[1]))
                else:
                    image = get_image(id[1])
                    await client.send_photo(chat_id=user_id,photo=image)