from pymongo import MongoClient
client = MongoClient('mongo')
db = client['312Project']
accounts = db["accounts"]
posts = db["posts"]
global_chat = db["global"]