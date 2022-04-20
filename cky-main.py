import pymongo

#including names, and password
uri = "mongodb://Group_4:ESSD8GMd3nLct74@cluster0-shard-00-00.qbwtc.mongodb.net:27017,cluster0-shard-00-01.qbwtc.mongodb.net:27017,cluster0-shard-00-02.qbwtc.mongodb.net:27017/mGroup_4?ssl=true&replicaSet=atlas-u0fo68-shard-0&authSource=admin&retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)   #pass in the uri

db = client['Student_information']
coll1 = db["student_names_collection"]

student1 = {'student_name': 'Student1', 'year_enrolled': 2020}
result = coll1.insert_one(student1)
client.close()

app