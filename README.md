# The Coctail Collection
 <div align="center"> 

[To wiew project deplyed on heroku](https://the-cocktail-collection.herokuapp.com/)
</div>



## Business goals of the site:

* At this point none existent. Affiliate Marketing could be added in the future.

## Visitor goals of the site:

* Find new interesting recepie to try.
* Look up multiple spots to decide on where to go.

## User Experience
 
Visitors of the site:
There are three main categories of Visitors
* Casual visitor, a visitor without much experience of makig cocktails.
* Enthusiast visitor, a visitor with an intrest in and experience of making cocktails.
* Professional visitor, a bartender or other such personel workning in the industry. 
 
As a casual visitor I want to find a recepie to try and make.
As a casual visitor I want to find a few recepies to dazzle my guests with in a upcoming party.
As a Enthusiast visitor I want to post my recepie and get critique or tips from other users.
As a Enthusiast visitor I want to find new recepie to try.
As a Enthusiast visitor I want to find new recepies to try and make my own version of.
As a Enthusiast visitor I want to post my recepies as a way of saving them for later use.
As a Professional user I want to find inspiration for a new cocktail to put on my menu.
As a Professional user I want to post my new recepie to get some qritique before putting it on my menu.

## Features 
#### Ingredients
* A populated database of over 400 ingredients that are used for creating new recipes. This collection of ingredients was created from calling https://www.thecocktaildb.com/ Api.
* Add ingredient page, where users can add their own ingredients to the database. The link to this hidden from users that are not logged in.
* Ingredient page, where an image and some basic information about the ingredient can be accessed.
#### Recipes
* A database for recepies that currently only has a few recepies on it.
* Add recipe page, where new recipes can be from the ingredients in the database. The link to this hidden from users that are not logged in.
* Display recipe page, where the recipe is displayed with an image, the glass to use, a list of ingredients with links to the ingreient page, and directions on how to make the cocktail.
For logged in users this page also features a comment section where comments can be posted, and for the author of the recipe there are buttons to delete comments and delete or edit the recipe.
#### User Registration and login
* Sign up page where visitors of the site can create a account to get access to posting comments and creating new recepies and ingredients.
* Sign in page where users that have registerd can log in to their accounts.


## Features to implement
* Advanced search, where users can seacrh for recepies based on ingredients or style of cocktail.
* Direct messaging, were users can send each other direct messages with tips or suggestions.
* User home page, Where users can uppload a profile picture and write about thier experience in the art of mixology.
* Most popular carousel on the homepage where the most visited recepies over the last week can be displayed.
* Clone button, that leads to a page similar to edit recepie, but instead saves as a new recepie, this would allow users to easily create their own version or a twist on a already existing cocktail.
* Tools used/recommended page where Affiliate links to tools can be posted so users can se what tools they need to buy.
* Rating system, where users can rate recepies 1-5 stars.
* Top list where the top rated recepies are displayed.
* Server side validation of the data to stop malicous users from insering things they shouldnt to the database.
* Admin account with privilges to delete any comments, ingrideints or recepies.
* Edit user, where users can change their password etc.
* Forgot password feature where a user can enter thir email and get a new password sent out.
* Collect Recipe feature, where users can create collections and fill them with recepies they like or want to try.
* Print menu, where users can print thier collection into a menu for a party.
* Print bar manual, where users can print a Bar manual to go along with the menu.

## Technologies used
This project uses HTML, CSS, JavaScript and Python programming languages.
#### [Gitpod online IDE](https://www.gitpod.io/)
This project was developed in Gitpod Online IDE
#### [Google fonts](https://fonts.google.com/)
This Project uses fonts from Google fonts.
#### [JQuery](https://jquery.com/)
This project uses jquery for DOM manipulation.
#### [Bootstrap](https://getbootstrap.com/)
This project uses bootstrap  for its grid system and premade classes.
#### [Pexels](https://www.pexels.com/search/ocean/)
This project uses Pexels as a free source of images.
#### [balsamiq Mockups](https://balsamiq.com/wireframes/)
This project uses balsamiq mockups 3 for creating wireframes.
#### [Flask](https://flask.palletsprojects.com/en/1.1.x/)
This project uses the Flask web framework.
#### [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
This project uses the Jinja template engine.
#### [MongoDB](https://www.mongodb.com/)
This project uses a MongoDB based database hosted on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
#### [Heroku](https://www.heroku.com/)
This project is hosted on Heroku.

Testing 