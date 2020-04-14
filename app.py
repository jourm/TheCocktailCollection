import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session, flash
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
    recepies = mongo.db.recepies.find()

    return render_template('home.html', recepies=recepies)


@app.route('/add_cocktail', methods=['GET', 'POST'])
def add_cocktail():
    if request.method == 'GET':
        return render_template('add_cocktail.html',
                               ingredients=mongo.db.ingredients.find())

    if request.method == 'POST':
        name = request.form['name']
        drink_type = request.form['type']
        ingredients = request.form.getlist('ingredients')
        ingredient_list = []
        for i in range(0, len(ingredients), 3):
            ingredient_list.append([ingredients[i], ingredients[i+1],
                                    ingredients[i+2]])
        directions = request.form['description']
        url = request.form['img-url']
        if 'user_id' in session:
            new_doc = {'name': name,
                       'drink_type': drink_type,
                       'ingredients': ingredient_list,
                       'directions': directions,
                       'img-url': url,
                       'author': session['user_id']}
        else:
            new_doc = {'name': name,
                       'drink_type': drink_type,
                       'ingredients': ingredient_list,
                       'directions': directions,
                       'img-url': url,
                       'author': ''}

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
    if 'user_id' in session:
        user = mongo.db.users.find_one({'_id': ObjectId(session['user_id'])})
        user['_id'] = str(user['_id'])
        return render_template('get_cocktail.html', cocktail=recepie,
                               user=user)
    return render_template('get_cocktail.html', cocktail=recepie, user=False)


@app.route('/edit_recepie/<recepie_id>', methods=['GET', 'POST'])
def edit_recepie(recepie_id):
    recepie = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
    if recepie['author'] == session['user_id']:
        if request.method == 'GET':
            counter = 0
            for ingredient in recepie['ingredients']:
                ingredient.append(mongo.db.ingredients.find_one({"_id":
                                                                 ObjectId(ingredient[2])})['ingredient'])
                ingredient.append(counter)
                counter += 1

            return render_template('edit_recepie.html', cocktail=recepie,
                                   counter=counter,
                                   ingredients=mongo.db.ingredients.find())

        if request.method == 'POST':
            name = request.form['name']
            drink_type = request.form['type']
            ingredients = request.form.getlist('ingredients')
            
            ingredient_list = []
            for i in range(0, len(ingredients), 3):
                ingredient_list.append([ingredients[i], ingredients[i+1],
                                        ingredients[i+2]])
            directions = request.form['description']
            url = request.form['img-url']
            if 'user_id' in session:
                new_doc = {'name': name,
                           'drink_type': drink_type,
                           'ingredients': ingredient_list,
                           'directions': directions,
                           'img-url': url,
                           'author': session['user_id']}
            else:
                new_doc = {'name': name,
                           'drink_type': drink_type,
                           'ingredients': ingredient_list,
                           'directions': directions,
                           'img-url': url,
                           'author': ''}

            mongo.db.recepies.update({'_id': ObjectId(recepie_id)}, new_doc)
            return redirect(url_for('get_recepie', recepie_id=recepie_id))
    else:
        flash('Not your recepie to edit')
        pass


@app.route('/delete_recepie/<recepie_id>')
def delete_recepie(recepie_id):
    cocktail = mongo.db.recepies.find_one({'_id': ObjectId(recepie_id)})
    if cocktail['author'] == session['user_id']:
        mongo.db.recepies.remove({'_id': ObjectId(recepie_id)})
        flash('Recepie Deleted')
        return redirect(url_for('home'))
    else:
        flash('You did not create this recepie!')


@app.route('/user_home')
def user_home():
    if 'username' in session:
        flash('you are logged in as' + session['username'])
        return 'you are logged in as' + session['username']

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                         login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            session['user_id'] = str(login_user['_id'])

            return redirect(url_for('user_home'))

    return 'Invail Email/Password combination'


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
                          'img-url': request.form['img-url'],
                          'collections': []})
            return redirect(url_for('user_home'))

        return 'That Username is already taken'
    return render_template


if __name__ == '__main__':
    app.secret_key = os.environ.get('SECRET')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
