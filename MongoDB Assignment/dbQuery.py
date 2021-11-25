from pymongo import MongoClient

mongo_client = MongoClient()
db = mongo_client.crashDB
col = db["relationalImport"]

print("Demonstrate access\n")
for x in col.find({ "Aircraft": "Farman F-60 Goliath" }):
    print(x) 
    print("\n")
input("Press enter to continue.")


print("\n\nDemonstrate access of sub document\n")
for x in col.find({ "Crashes.Location": "Pemberville, Ohio"}):
    print(x)
    print("\n")
input("Press enter to continue.")


print("\n\nDemonstrate sort and aggregate\n")
for x in col.aggregate([
    { "$match": {"Crashes.Casulaties.Aboard": "2"}},
    { "$sort": {"Crashes.Casulaties.Aboard" : -1}}
    ]):

    print(x)
    print("\n")
input("Press enter to continue.")

