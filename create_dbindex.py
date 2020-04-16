import requests
import json
import pymongo
from bson.objectid import ObjectId
import os
import re
from os import path
if path.exists("env.py"):
    import env

# This file houses the code used to connect to Mongodb and create a 
# searcheable index based on the name key in the recepies collection.

MONGO_URI = os.environ.get("MONGO_URI")
DBS_NAME = "TheCocktailCollection"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could Not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME]['recepies']

coll.create_index([('name', 'text')], default_language="english")
