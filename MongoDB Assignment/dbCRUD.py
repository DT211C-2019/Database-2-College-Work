from pymongo import MongoClient

mongo_client = MongoClient()
db = mongo_client.crashDB
col = db["relationalImport"]

print("Adding 'Space Shuttle' to the DB\n")
col.insert_one({"Aircraft": "Space Shuttle"})
input("Press enter to continue\n")

print("Updating 'Space Shuttle' to 'Space Shuttle Mk2\n")
col.update_one({"Aircraft": "Space Shuttle"}, {"$set": {"Aircraft": "Space Shuttle Mk2"}})
input("Press enter to continue\n")

print("Removing 'Space Shuttle Mk2'\n")
col.delete_one({"Aircraft": "Space Shuttle Mk2"})