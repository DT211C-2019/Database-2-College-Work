import csv
from pymongo import MongoClient

# Constants
csv_path = "C:/Users/Solon/Desktop/Projects/College/Year3/Database-2-College-Work/MongoDB Assignment/Airplane_Crashes_and_Fatalities_Since_1908.csv"

csvfile = open(csv_path, 'r')
reader = csv.DictReader(csvfile)
reader = list(reader)
mongo_client = MongoClient()
db = mongo_client.crashDB
db.relationalImport.drop()

# Finds all unique aircraft
unique = []


def findUnique():
    print("Starting unique element indexing...")
    for X in reader:
        if X["Type"] not in unique:
            unique.append(X["Type"])
            db.relationalImport.insert_one(
                {"Aircraft": X["Type"], "Crashes": []})
    print("Unqiue elements found!")


# Adds all instances as sub-documents to aircraft document
def addToDB():
    print("Starting instance export...")
    for Y in reader:
        if Y["Type"] in unique:
            db.relationalImport.update_one(
                {"Aircraft": Y["Type"]},
                {"$push":
                 {"Crashes": {
                     "Datetime": {
                         "Date": Y["Date"],
                         "Time": Y["Time"],
                     },
                     "Casualties": {
                         "Aboard": Y["Aboard"],
                         "Ground": Y["Ground"],
                     },
                     "Operator_Data": {
                         "Flight No.": Y["Flight #"],
                         "Route": Y["Route"],
                         "Registration": Y["Registration"],
                         "CN/IN": Y["cn/In"],
                     },
                     "Operator": Y["Operator"],
                     "Location": Y["Location"],
                     "Summary": Y["Summary"]

                 }}}
            )
    print("Unique instances added!")


# Driver code
findUnique()
addToDB()
