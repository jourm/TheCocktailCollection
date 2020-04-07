from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from os import path
if path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'TheCocktailCollection'
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)


@app.route('/')
@app.route('/add_ingredient')
def add_ingredient():
    return render_template('')


def insert_ingredient(ingredient):
    mongo.db.ingredients.insert_one(ingredient)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
