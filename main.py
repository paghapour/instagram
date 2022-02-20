from http import client
import profile
import pymongo

client = pymongo.MongoClient('mongo://localhost:27017/')

mydb = client["instagram"]
mycol = mydb["profile"]

profile= [{"_userid" : "1" ,
          "username" : "pooria" ,
          "fullname": "pooriaaghapour" ,
          "biography" : "example" ,
          "total_followers" : "20" ,
          "total_followees" : "10" ,
          "media_count" : "3" ,
          "update_at" : "datetime" ,
          "create_at" : "datetime"
          },
          {"_userid" : "2" ,
          "username" : "arshia" ,
          "fullname": "arshiaaghapour" ,
          "biography" : "example" ,
          "total_followers" : "30" ,
          "total_followees" : "40" ,
          "media_count" : "7" ,
          "update_at" : "datetime" ,
          "create_at" : "datetime"
          }]
#mycol.insert_many(profile)
dlt = {'username' : "arshia"}
mycol.delete_one(dlt)

