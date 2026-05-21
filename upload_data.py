from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://thapadheeraj857_db_user:Dheeraj123@cluster001.15qn1hx.mongodb.net/?appName=Cluster001"

# create client and connect  to server
client = MongoClient(uri)

# create database and collection name
DATABASE_NAME = "Dheeraj"
COLLECTION_NAME = "waferfault"

df = pd.read_csv(r"notebooks\wafer_file.csv")
df = df.drop('Unnamed: 0',axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
