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


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could Not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

ingredients = coll.find()

for ingredient in ingregients:
    new ingredient = {"ingredient": value[0]['strIngredient'].lower(),
                      "description": value[0]['strDescription'],
                      "type": value[0]['strType'],
                      "alcohol": value[0]['strAlcohol'],
                      "abv": value[0]['strABV']}

