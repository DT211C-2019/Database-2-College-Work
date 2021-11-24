from pymongo import MongoClient

mongo_client = MongoClient()
db = mongo_client.crashDB
col = db["relationalImport"]

for x in col.find({ "Aircraft": "Farman F-60 Goliath" }):
    print(x)