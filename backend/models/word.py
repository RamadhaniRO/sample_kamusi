from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['swahili-app']
words_collection = db['words']

def find_word(word):
    return words_collection.find_one({"word": word})
