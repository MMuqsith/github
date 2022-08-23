import  pymongo
client = pymongo.MongoClient("mongodb+srv://Muqsith:muqsith@cluster0.8s7vgd5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={"name":"Muqsith",
   "email":"muhammedmuqsith999@gmail.com",
   "surname": "Muqs"}

db1=client["mongotest"]
coll=db1["test"]
coll.insert_one(d)