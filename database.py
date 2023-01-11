from pymongo import MongoClient
from config import * 

client = MongoClient(mongodb_key)
user_db = client.data.user
status_db = client.data.status
message_db = client.data.message
class database:
    def append_user(id:int,name:str) -> None:
        ''' 
            Append user id to the database.
            Args:
                id : telegram id of the user.
        '''
        if user_db.find_one({"id":id}) == None :
            user_db.insert_one({"id":id,"name":name,"language":"undefine"}) # add user to the database         

    def get_user(id:int) -> dict:
        '''
            Get the user data from the database.
            Args:
                id : Telegram id of ther user.
            Return:
                dictionary data of the user in database.
        '''
        return user_db.find_one({"id":id})
    
    def edit_language(id:int,language:str) -> None:
        '''
            Edit the language user prefer of the database.
            Args:
                id: Telegam id of user.
                language: Language.
        '''
        user_db.update_one({"id":id},{"$set":{"language":language}})
    
    def remove(id:int) -> None:
        '''
            Remove user from the database.
            Args:
                id: telegram id of the user.
        '''
        user_db.delete_one({"id":id})
    

    def active_member() -> int:
        '''
            Return the acitve user of the bot.
        '''
        return len(list(user_db.find()))
    def users_id() -> dict:
        '''
           Return all users_id in the database
        '''
        return  [id["id"] for id in list(user_db.find())]
    def add_message(message_id:int,data:str) -> None:
        message_db.insert_one({"message_id":message_id,"data":data})
    def update_message(message_id:int,data:str) -> None:
        '''
            Update data for a given id
            Args:
                message_id: id of a message
                data: state data of a message
        '''
        message_db.update_one({"message_id":message_id},{"$set":{"data":data}})
    def message_status(message_id:int,) -> dict:
        '''
        Get a data of a given id
        Args:
            message_id: id of a message
        Return:

        '''
        return message_db.find_one({"message_id":message_id})
        