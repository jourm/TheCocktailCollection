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
def home():
    return render_template('home.html')


@app.route('/add_cocktail', methods=['GET', 'POST'])
def add_cocktail():
    if request.method == 'GET':
        return render_template('add_cocktail.html',
                               ingredients=mongo.db.ingredients.find())
    if request.method == 'POST': 
        print(request.form)
        mongo.db.recepie.insert_one(request.form)
        return render_template('add_cocktail.html',
                               ingredients=mongo.db.ingredients.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
