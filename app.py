import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
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
                   'ingredients': ingredient_list,
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


@app.route('/get_ingredient/<ingredient_id>')
def get_ingredient(ingredient_id):
    ingredient = mongo.db.ingredients.find_one(
        {"_id": ObjectId(ingredient_id)})
    return render_template('get_ingredient.html', ingredient=ingredient)


@app.route('/get_recepie/<recepie_id>')
def get_recepie(recepie_id):
    recepie = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})

    for ingredient in recepie['ingredients']:
        ingredient.append(mongo.db.ingredients.find_one({"_id":
                                                         ObjectId(ingredient[2])})['ingredient'])
    return render_template('get_cocktail.html', cocktail=recepie)


@app.route('/edit_recepie/<recepie_id>')
def edit_recepie(recepie_id):
    recepie = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
    counter = 0
    for ingredient in recepie['ingredients']:
        ingredient.append(mongo.db.ingredients.find_one({"_id":
                                                         ObjectId(ingredient[2])})['ingredient'])
        ingredient.append(counter)
        counter += 1

    return render_template('edit_cocktail.html', cocktail=recepie,
                           counter=counter,
                           ingredients=mongo.db.ingredients.find())


@app.route('/user_home')
def user_home():
    if 'email' in session:
        return 'you are logged in as' + session['email']

    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email': request.form['email']})

        if existing_user is None:
            hashpassword = bcrypt.hashpw(request.form['password']
                                         .encode('utf-8'), bcrypt.gensalt())
            users.insert({'email': request.form['email'],
                          'username': request.form['username'],
                          'password': hashpassword,
                          'img-url': request.form['img-url']})
            session['email'] = request.form['email']
            return redirect(url_for('user_home'))

        return 'that email anddress is already in use'
    return render_template


if __name__ == '__main__':
    app.secret_key = os.environ.get('SECRET')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
