import requests
import json
import pymongo
from bson.objectid import ObjectId
import os
import re
from os import path
if path.exists("env.py"):
    import env

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
coll = conn[DBS_NAME]


def getnewdrink(id):
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i='
        + str(id))

    for drink in response.json().values():

        if drink is None:
            return False
        else:
            ingredient_list = []
            for i in range(1, 15):
                if drink[0]['strIngredient' + str(i)]:
                    if drink[0]['strMeasure' + str(i)]:
                        a, b, c = re.split(r"([a-z])",
                                           drink[0]['strMeasure' + str(i)], 1, re.I)
                        new_ingredient = [a]
                        new_ingredient.append(b+c)
                    else:
                        new_ingredient = ["", ""]

                    ing = coll['ingredients_new'].find_one(
                        {'ingredient': drink[0]['strIngredient' + str(i)]
                         .lower()})
                    new_ingredient.append(str(ing['_id']))
                    ingredient_list.append(new_ingredient)

            drink_ = {'name': drink[0]['strDrink'],
                      'glass_type': drink[0]['strGlass'],
                      'ingredients': ingredient_list,
                      'directions': drink[0]['strInstructions'],
                      'img-url': drink[0]['strDrinkThumb'],
                      'author': '5e91e4fd0a2edbd3b2146d35',
                      'comments': []}
            return drink_


for i in range(11001, 20000):
    try:
        drink = getnewdrink(i)
        coll['recepies'].insert_one(drink)
        print(i)
    except:
        continue



