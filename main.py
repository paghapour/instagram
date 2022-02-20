from http import client
import profile
import pymongo

client = pymongo.MongoClient('mongo://localhost:27017/')

mydb = client["instagram"]
mycol = mydb["profile"]
