from pymongo import MongoClient

client = MongoClient()
db = client['okcoindb']
collection = db['prices']

result = collection.delete_many({})
print result.deleted_count
