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
COLLECTION_NAME = "ingredients"


def getnewingredient(id):
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid='
        + str(id))

    for value in response.json().values():
    
        if value is None:
            return False
        else:
            return{"ingredient": value[0]['strIngredient'],
                   "description": value[0]['strDescription'],
                   "type": value[0]['strType'],
                   "alcohol": value[0]['strAlcohol'],
                   "abv": value[0]['strABV']}


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is COnnected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could Not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

for i in range(601, 1000):

    new_ingredient = getnewingredient(i)
    if new_ingredient is False:
        continue
    coll.insert_one(new_ingredient)
