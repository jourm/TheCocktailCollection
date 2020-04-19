import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import os
from os import path
if path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MONGO_DBNAME'] = 'TheCocktailCollection'
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)


@app.route('/')
def home():
    recipes = mongo.db.recepies.find().sort('_id', pymongo.ASCENDING).limit(30)
    return render_template('home.html', recipes=recipes)


@app.route('/search', methods=['POST'])
def search():
    recipes = mongo.db.recepies.find({"$text": {"$search":
                                      request.form['name']}})
    
    if recipes.count() >= 1:
        return render_template('home.html', recipes=recipes)
    ingredient = mongo.db.ingredients_new.find({'ingredient':
                                                request.form['name']})
    if ingredient.count() == 1:
        return render_template('get_ingredient.html', ingredients=ingredient)
    else: 
        return render_template('no_result.html')


@app.route('/create_new_recipe', methods=['GET', 'POST'])
def create_new_recipe():
    if request.method == 'GET':
        return render_template('create_new_recipe.html',
                               ingredients=mongo.db.ingredients_new.find())

    elif request.method == 'POST':
        name = request.form['name']
        glass_type = request.form['glass_type']
        ingredients = request.form.getlist('ingredients')
        ingredient_list = []
        for i in range(0, len(ingredients), 3):
            ingredient_list.append([ingredients[i], ingredients[i+1],
                                    ingredients[i+2]])
        directions = request.form['description']
        url = request.form['img-url']
        if 'user_id' in session:
            new_doc = {'name': name,
                       'glass_type': glass_type,
                       'ingredients': ingredient_list,
                       'directions': directions,
                       'img-url': url,
                       'author': session['user_id'],
                       'comments': []}
        else:
            new_doc = {'name': name,
                       'glass_type': glass_type,
                       'ingredients': ingredient_list,
                       'directions': directions,
                       'img-url': url,
                       'author': '',
                       'comments': []}

        mongo.db.recepies.insert_one(new_doc)
        return render_template('create_new_recipe.html',
                               ingredients=mongo.db.ingredients_new.find())


@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'GET':
        return render_template('add_ingredient.html',
                               ingType=mongo.db.ingType.find())
    if request.method == 'POST':
        mongo.db.ingredients_new.insert_one(request.form.to_dict())
        return render_template('add_ingredient.html',
                               ingType=mongo.db.ingType.find())


@app.route('/get_ingredient/<ingredient_id>')
def get_ingredient(ingredient_id):
    ingredient = mongo.db.ingredients_new.find(
        {"_id": ObjectId(ingredient_id)})
    return render_template('get_ingredient.html', ingredients=ingredient)


@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    recipe = mongo.db.recepies.find_one({"_id": ObjectId(recipe_id)})
    for ingredient in recipe['ingredients']:
        ingredient.append(
            mongo.db.ingredients_new.find_one({"_id":
                                               ObjectId(ingredient[2])})['ingredient'])
    if 'user_id' in session:
        user = mongo.db.users.find_one({'_id': ObjectId(session['user_id'])})
        user['_id'] = str(user['_id'])
        return render_template('get_recipe.html', recipe=recipe,
                               user=user)
    return render_template('get_recipe.html', recipe=recipe, user=False)


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = mongo.db.recepies.find_one({"_id": ObjectId(recipe_id)})
    if recipe['author'] == session['user_id']:
        if request.method == 'GET':
            counter = 0
            for ingredient in recipe['ingredients']:
                ingredient[0] = ingredient[0].rstrip()
                ingredient.append(mongo.db.ingredients_new.find_one
                                  ({"_id":
                                    ObjectId(ingredient[2])})['ingredient'])
                ingredient.append(counter)
                counter += 1

            return render_template('edit_recipe.html', recipe=recipe,
                                   counter=counter,
                                   ingredients=mongo.db.ingredients_new.find())

        if request.method == 'POST':
            name = request.form['name']
            glass_type = request.form['glass_type']
            ingredients = request.form.getlist('ingredients')

            ingredient_list = []
            for i in range(0, len(ingredients), 3):
                ingredient_list.append([ingredients[i], ingredients[i+1],
                                        ingredients[i+2]])
            directions = request.form['description']
            url = request.form['img-url']
            if 'user_id' in session:
                new_doc = {'name': name,
                           'glass_type': glass_type,
                           'ingredients': ingredient_list,
                           'directions': directions,
                           'img-url': url,
                           'author': session['user_id']}
            else:
                new_doc = {'name': name,
                           'glass_type': glass_type,
                           'ingredients': ingredient_list,
                           'directions': directions,
                           'img-url': url,
                           'author': ''}

            mongo.db.recepies.update({'_id': ObjectId(recipe_id)}, new_doc)
            return redirect(url_for('get_recipe', recipe_id=recipe_id))
    else:
        flash('Not your recipe to edit')
        pass


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    cocktail = mongo.db.recepies.find_one({'_id': ObjectId(recipe_id)})
    if cocktail['author'] == session['user_id']:
        mongo.db.recepies.remove({'_id': ObjectId(recipe_id)})
        flash('recipe Deleted')
        return redirect(url_for('home'))
    else:
        flash('You did not create this recipe!')


@app.route('/add_comment/<recipe_id>', methods=['POST'])
def add_comment(recipe_id):
    if 'username' in session:
        recipe = mongo.db.recepies.find_one({'_id': ObjectId(recipe_id)})
        comment = {'username': session['username'],
                   'message': request.form['message']}
        recipe['comments'].append(comment)
        mongo.db.recepies.update({'_id': ObjectId(recipe_id)}, recipe)
    return redirect(url_for('get_recipe', recipe_id=recipe_id))


@app.route('/delete_comment/<recipe_id>', methods=['POST'])
def delete_comment(recipe_id):
    recipe = mongo.db.recepies.find_one({'_id': ObjectId(recipe_id)})
    username = request.form['username']
    message = request.form['message_d']
    recipe['comments'].remove({'username': username,
                                'message': message})
    mongo.db.recepies.update({'_id': ObjectId(recipe_id)}, recipe)
    return redirect(url_for('get_recipe', recipe_id=recipe_id))


@app.route('/user_home')
def user_home():
    if 'username' in session:       
        return redirect(url_for('home'))
    else:
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
        if 'username' in session:
            return redirect(url_for('home'))
        else:
            return render_template('register.html')
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

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
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.secret_key = os.environ.get('SECRET')
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")), 
            debug=True)
