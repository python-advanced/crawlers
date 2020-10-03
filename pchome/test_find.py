import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.pchome
coll = db.products

coll.find({'age': 35})

# name containing asus
name_condition = {'name': {'$regex': '.*asus.*', '$options': 'i'}}
# data = coll.find(name_condition)

price_condition = {'price': {'$gt': 10000}}
# data = coll.find(price_condition)

# and operator example
data = coll.find({'$and': [name_condition, price_condition]})
for d in data:
    print(d['name'], d['price'])


# coll.update_one({'name': 'ASUS XG32VQR(低藍光+不閃屏)'}, {'$set': {'price': 8000}}, upsert=True )

# upsert example (insert if not exist)
# coll.update_one({'name': 'Allen'}, {'$set': {'name': 'Allen'}}, upsert=True)

# delete example
# coll.delete_one({'name': 'Allen'})
