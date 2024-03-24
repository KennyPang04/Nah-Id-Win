from pymongo import MongoClient

class Chat:
    # Parameters:
    # Database - the mongodb client chat database = mongo_client["cse312"]
    # Title - name of the chat = string
    def __init__(self, database: MongoClient, title: str):
        chat_collection = database[title]
        
    def store_chat(self):
        print("hi")