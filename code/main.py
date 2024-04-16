from pymongo import MongoClient
client = MongoClient()
db = client.mydatabase
collection = db.mycollection
doc = {"name": "vijayagokul", "age": 3, "city": "New york"}
# result = collection.insert_one(doc)
print(result.inserted_id)

docs = [
    {"name": "mike", "age": 32, "city": "san fransisco"},
    {"name": "fizz", "age": 25, "city": "kasimedu"},
    {"name": "nags", "age": 14, "city": "avadi"},
    {"name": "saec", "age": 26, "city": "sennerkuppam"},

]
result = collection.insert_many(docs)
print(result.inserted_ids)

result = collection.find_one()
print(result)

result = collection.find one({"name": "john"})
print(result)

results = collection.find({"age": {"$gt": 30}})

for r in results:
    print(r)

results=collections.find({"age":{"$lt":30}})
for r in results:
    print(r)

results=collection.find({"age":{"$gt":25} and {"$lt":30}})
for r in results:
    print(r)

results=collection.find({"age":{"$gte":25}})
for r in results:
    print(r)

results=collection.find({"age":{"$lte":20}})
for r in results:
    print(r)

result = collection.find({"age":{"$exists":"true"}})
for r in results:
    print(r)

results = collection.find().sort({"age":1})
for r in results:
    print(r)

results = collections.find().sorts({"age":1}).skip(2)
for r in results:
    print(r)

criteria = {"name": "john"}
new_values = {"$set": {"age": 31}}
collection.update_one(criteria, new_values)

results = collections.find(criteria)
for r in result:
    print(r)

criteria = {"age": {"$lt": 30}}
new_values = {"$inc": {"age": 1}}
collection.update_many(criteria, new_values)

result = collection.find({"age":{"$lte":30}})
for r in result:
    print(r)

collection.delete_one({"name":"join"})

collection.delete_many({"age":})


    