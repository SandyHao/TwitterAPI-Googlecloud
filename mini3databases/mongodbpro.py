import pymongo
import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mini3mongo"]
# db.createCollection("tweetsinquiry",{autoIndexId:true})
'''
document=({"titles":['username','tweetname','tweetsnumber','keyword1','keyword2','keyword3','keyword4','keyword5','keyword6']});
'''
username="Mac"
tweetname="sichun"
tweetsnumber=20
keyword1="model"
keyword2="beauty"
keyword3="tall"
keyword4="hair"
keyword5= "curly"
keyword6="children"
#print(datetime.datetime.now())
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mini3mongo"]
mycol = mydb["tweetsinquiry"]
record = {"time":datetime.datetime.now(),"username":username,"tweetname":tweetname,"tweetsnumber":tweetsnumber,
        "keyword1":keyword1,"keyword2":keyword2,"keyword3":keyword3,"keyword4":keyword4,
        "keyword5":keyword5,"keyword6":keyword6}
x=mycol.insert_one(record)
