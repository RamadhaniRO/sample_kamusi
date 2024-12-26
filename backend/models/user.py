from pymongo import MongoClient
from flask_bcrypt import Bcrypt

client = MongoClient('mongodb://localhost:27017/')
db = client['swahili-app']
users_collection = db['users']
bcrypt = Bcrypt()

class User:
    @staticmethod
    def create_user(email, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users_collection.insert_one({"email": email, "password": hashed_password})

    @staticmethod
    def find_user(email):
        return users_collection.find_one({"email": email})
