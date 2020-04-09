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
        name = request.form['name']
        drink_type = request.form['type']
        ingredients = request.form.getlist('ingredients')
        print(ingredients)
        ingredient_list = []
        for i in range(0, len(ingredients), 3):
            ingredient_list.append([ingredients[i], ingredients[i+1],
                                    ingredients[i+2]])
        directions = request.form['description']
        url = request.form['img-url']

        new_doc = {'name': name,
                   'drink_type': drink_type,
                   'ingredeients': ingredient_list,
                   'directions': directions,
                   'img-url': url}
        mongo.db.recepies.insert_one(new_doc)
        return render_template('add_cocktail.html',
                               ingredients=mongo.db.ingredients.find())


@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'GET':
        return render_template('add_ingredient.html',
                               ingType=mongo.db.ingType.find())
    if request.method == 'POST':
        mongo.db.ingredients.insert_one(request.form.to_dict())
        return render_template('add_ingredient.html',
                               ingType=mongo.db.ingType.find())


@app.route('/display_ingredient/<ingredient_id>')
def get_ingredient(ingredient_id):
    ingredient = mongo.db.ingredients.find_one({"_id": ObjectId(ingredient_id)})
    return render_template('get_ingredient.html', ingredient=ingredient)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
