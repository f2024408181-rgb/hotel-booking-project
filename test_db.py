from pymongo import MongoClient

MONGO_URL = "mongodb+srv://raijin:hello123@cluster0.n3gedq5.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(MONGO_URL)

    db = client.test_database

    collection = db.test_collection

    collection.insert_one({"test": "working"})

    print("SUCCESS: MongoDB Connected!")

except Exception as e:
    print("ERROR:")
    print(e)
