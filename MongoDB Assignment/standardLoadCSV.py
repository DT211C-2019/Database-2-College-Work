import csv
from pymongo import MongoClient

# Constants
csv_header = ["Date", "Time", "Location", "Operator", "Flight #", "Route",
              "Type", "Registration", "cn/In", "Aboard", "Fatalities", "Ground", "Summary"]
csv_path = "C:/Users/Solon/Desktop/Projects/College/Year3/Database-2-College-Work/MongoDB Assignment/Airplane_Crashes_and_Fatalities_Since_1908.csv"

csvfile = open(csv_path, 'r')
reader = csv.DictReader(csvfile)
mongo_client = MongoClient()
db = mongo_client.crashDB
db.standardImport.drop()

print('Starting export...')

for each in reader:
    row = {}
    for field in csv_header:
        row[field] = each[field]

    db.standardImport.insert_one(row)

print('Done!')
