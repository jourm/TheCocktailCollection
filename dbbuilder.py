import requests
import json
import pymongo
from bson.objectid import ObjectId
import os
from os import path
if path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DBS_NAME = "TheCocktailCollection"
COLLECTION_NAME = "ingredients_new"
""" This pythonfile when run fills the ingType and ingredients_new of the mongodb cluster specified in env.py"""


def getnewingredient(id):
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid='
        + str(id))

    for value in response.json().values():
    
        if value is None:
            return False
        else:
            return{"ingredient": value[0]['strIngredient'].lower(),
                   "description": value[0]['strDescription'],
                   "type": value[0]['strType'],
                   "alcohol": value[0]['strAlcohol'],
                   "abv": value[0]['strABV'],
                   "img-url": "https://www.thecocktaildb.com/images/ingredients/" +
                   value[0]['strIngredient'] + "-Medium.png"}


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could Not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]
coll_intype = conn[DBS_NAME]['ingType']


categories = []
for i in range(1, 1000):
    new_ingredient = getnewingredient(i)
    if new_ingredient is False:
        continue
    else:
        if new_ingredient['type'] not in categories:
            categories.append(new_ingredient['type'])
        coll.insert_one(new_ingredient)


for i in categories:
    coll_intype.insert_one({'name': i})
