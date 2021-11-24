import csv
from os import read
from typing import Type
from pymongo import MongoClient
from bson.son import SON

# Constants
csv_header = ["Date", "Time", "Location", "Operator", "Flight #", "Route",
              "Type", "Registration", "cn/In", "Aboard", "Fatalities", "Ground", "Summary"]
csv_path = "C:/Users/Solon/Desktop/Projects/College/Year3/Database-2-College-Work/MongoDB Assignment/Airplane_Crashes_and_Fatalities_Since_1908.csv"

csvfile = open(csv_path, 'r')
reader = csv.DictReader(csvfile)
reader = list(reader)
mongo_client = MongoClient()
# Replace "crashDB" with whatever you want to name the database
db = mongo_client.crashDB
# Replace all instances of "relationalImport" with whatever you want to name your collection
db.relationalImport.drop()

unique = []


def findUnique():
    for X in reader:
        if X["Type"] not in unique:
            unique.append(X["Type"])
            db.relationalImport.insert_one(
                {"Aircraft": X["Type"], "Crashes": []})
    print("Unqiue elements found!")


def addToDB():
    for Y in reader:
        if Y["Type"] in unique:
            row = {}

            row["Date"] = Y["Date"]
            row["Time"] = Y["Time"]
            row["Location"] = Y["Location"]
            row["Operator"] = Y["Operator"]
            row["Flight #"] = Y["Flight #"]
            row["Route"] = Y["Route"]
            row["Registration"] = Y["Registration"]
            row["cn/In"] = Y["cn/In"]
            row["Aboard"] = Y["Aboard"]
            row["Fatalities"] = Y["Fatalities"]
            row["Ground"] = Y["Ground"]
            row["Summary"] = Y["Summary"]

            db.relationalImport.update_one(
                {"Aircraft": Y["Type"]},
                {"$push":
                 {"Crashes": {
                     "Date": Y["Date"],
                     "Time": Y["Time"],
                     "Location": Y["Location"],
                     "Operator": Y["Operator"],
                     "Flight No.": Y["Flight #"],
                     "Route": Y["Route"],
                     "Registration": Y["Registration"],
                     "CN/IN": Y["cn/In"],
                     "Aboard": Y["Aboard"],
                     "Fatalities": Y["Fatalities"],
                     "Ground": Y["Ground"],
                     "Summary": Y["Summary"]

                 }}}
            )
    print("Unique instances added")


findUnique()
addToDB()
