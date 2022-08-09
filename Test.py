import pymongo

client = pymongo.MongoClient("mongodb+srv://Suraj_1995:YRVmEpe5qnKSrR7h@cluster0.b7sbevw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name": "suraj",
    "email": "kashyapsrj@gmail.com",
    "surname": "kashyap"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

