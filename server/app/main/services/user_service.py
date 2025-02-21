from pymongo import MongoClient
from ..config import Config



class UserService:
    def __init__(self):
        self.__mongo_client = MongoClient(Config.MONGODB_URI)
        self.__mongo_db = self.__mongo_client.get_database()
        self.__users_collection = self.__mongo_db.get_collection("users")

    def find_or_create_user(self, email, name, picture, user_id):
        user = self.__users_collection.find_one({"email": email}, {"_id": 0})
        if not user:
            user = {"email": email, "name": name, "picture": picture, "user_id": user_id, "is_admin": False}
            self.__users_collection.insert_one(user)
            return user
        return user

    def find_by_email(self, email):
        user = self.__users_collection.find_one({"email": email}, {"_id": 0})
        return user
