from pymongo import MongoClient
from config import * 

client = MongoClient(mongodb_key)
user_db = client.data.user
status_db = client.data.status

class database:
    def append_user(id:int,name:str) -> None:
        ''' 
            Append user id to the database.
            Args:
                id : telegram id of the user.
        '''
        if user_db.find_one({"id":id}) == None :
            user_db.insert_one({"id":id,"name":name,"language":"undefine"}) # add user to the database  
            member =  status_db.find_one({"status_object":True})["member"] # get the value of all user that start the bot 
            status_db.update_one({"member":member},{"$set":{"member":member+1}})       

    def get_user(id:int) -> None:
        '''
            Get the user data from the database.
            Args:
                id : Telegram id of ther user.
            Return:
                dictionary data of the user in database.
        '''
        return user_db.find_one({"id":id})
    
    def edit_language(id:int,language:str) :
        '''
            Edit the language user prefer of the database.
            Args:
                id: Telegam id of user.
                language: Language.
        '''
        user_db.update_one({"id":id},{"$set":{"language":language}})
    
    def remove(id:int):
        '''
            Remove user from the database.
            Args:
                id: telegram id of the user.
        '''
        user_db.delete_one({"id":id})
    

    def active_member():
        '''
            Return the acitve user of the bot.
        '''
        return len(list(user_db.find()))
    def users_id():
        '''
           Return all users_id in the database
        '''
        return  [id["id"] for id in list(user_db.find())]

