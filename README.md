# The Cocktail Collection
 <div align="center"> 

[To wiew project deplyed on heroku](https://the-cocktail-collection.herokuapp.com/)
</div>

![Image of landingpage](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/landingpage.png)

Making cocktails is a fun and rewardung hobby enjoyed by many. 
There is for exaple a large subreddit about the subject that is very active.
The Cocktail collection is a community driven site dedicated to cocktails and was developed as a full stack education project using
Html, Css, JavaScript for the frontend, Python and Flask for the backend and a Mongodb based Database.
The main purpuse was to learn and demonstrate database handeling in a NoSQL enviroment using python.
Therefore, more focus has been placed on the datastructure and backend than the frontend. 


## Business goals of the site:

* At this point none existent. Affiliate Marketing could be added in the future.

## Visitor goals of the site:

* Find new interesting recepie to try.
* Save recipes for later.
* Post recipes to get critique on.

## User Experience
 
### Visitors of the site:
There are three main categories of Visitors
* Casual visitor, a visitor without much experience of makig cocktails.
* Enthusiast visitor, a visitor with an intrest in and experience of making cocktails.
* Professional visitor, a bartender or other such personel workning in the industry. 
### User stories
* As a casual visitor I want to find a recepie so that I can try and make it.
* As a casual visitor I want to find a few recepies so that I can dazzle my guests with them in a upcoming party.
* As a Enthusiast visitor I want to find new recepie so that I can try it.
* As a Enthusiast visitor I want to find new recepies so that I can try and make my own version of.
* As a Enthusiast visitor I want to post my recepie so that I can get critique or tips from other users.
* As a Enthusiast visitor I want to post my recepies so that I can save them for later use.
* As a Professional user I want to find inspiration for a new cocktail so that I can put it on my menu.
* As a Professional user I want to post my new recepie so that I can get some qritique before putting it on my menu.

## Wireframes
Thsese wireframes were created as a base for the project and the actual views may vary some.
* [Landing Page](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/wireframes/landing_page.PNG)
* [Recipe Page](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/wireframes/recipe_page.PNG)
* [Ingredient Page](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/wireframes/ingredient_page.PNG)
* [Create/Edit Recepie Page](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/wireframes/create_edit_recepie.PNG)
* [Create Ingredient Page](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/wireframes/create_new_ingredient.PNG)
* [Register Page](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/wireframes/register.PNG)
* [Sign in Page](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/wireframes/singin.PNG)

## Design Choises
Since the main focus in this project has been backend and databse handeling a basic Bootstrap theme was used to provide the majority f the styling in this project.
A dark theme with Mint accents was chosen to keep the site looking modern and clean. To add some modern and "bespoke" feeling to the site, a blurry black and white image of a barshelf was added as a background immage for all pages.
If there was more time spent on this project, more custom css, fonts etc could be edited to further improve the feel of the site.

## Features 
#### Navbar
* Avliable on all pages and features links for Home, Sign In, Sign up and a searchbar for users not logged in and Home, Create New Recipe, Add Ingredient, Sign out and A searchbar for users that have been logged in.

#### Ingredients
* A Mongodb collection of over 400 ingredients that are used for creating new recipes. This collection of ingredients was created from https://www.thecocktaildb.com/ Api.
* Add ingredient page, where users can add their own ingredients to the database. The link to this hidden from users that are not logged in.
* Ingredient page, where an image and some basic information about the ingredient can be accessed.
#### Recipes
* A Mongodb collection of over 400 recipes with a text based index making the collection searcheable. This collection of recipes was created from https://www.thecocktaildb.com/ Api.
* Create new recipe page, where new recipes can be created from the ingredients in the database. This page features a form that is expanded when more ingredients are added using javascript. The form uses
 a few different input types to steer the user to input the correct data form as well as some html verification.
But there is currently no serverside valification to block malicous users. The link to this hidden from users that are not logged in.
* Edit recepie page, very similar to add recipe page, but filled out with the recipe to edit and only avliable to the author of a recipe from the recipe page. This page features a form that is expanded when more ingredients are added using javascript. The form uses
 a few different input types to steer the user to input the correct data form as well as some html verification.
But there is currently no serverside valification to block malicous users. The link to this hidden from users that are not logged in.
* Display recipe page, where the recipe is displayed with an image, the glass to use, a list of ingredients with links to the ingreient page, and directions on how to make the cocktail.
For logged in users this page also features a comment section where comments can be posted, and for the author of the recipe there are buttons to delete comments and delete or edit the recipe.
#### User Registration and login
* Sign up page where visitors of the site can create a account to get access to posting comments and creating new recepies and ingredients.
* Sign in page where users that have registerd can log in to their accounts.
#### The Database:
![database](https://github.com/jourm/TheCocktailCollection/blob/master/static/images/wireframes/Datastructure.png)
This is a visual representation of the database that shows its structure, It features 4 collections, Recipes, Ingredients, Users and Igredeint types, as well as plans for expansion.
It is a non relational database, but there are some cases where an id of items in another collection are stored for improved stability if there are chnages to those items. As is visible in the image there are plans for expansion od the database.


## Features to implement
Here are a list of features to imlement, in no particular order, to improve the functionality of the site.
* Advanced search, where users can seacrh for recepies based on ingredients or style of cocktail. This advanced search would have a feature where users can input what they have at home and get recipes containing those ingredients.
* Direct messaging, were users can send each other direct messages with tips or suggestions.
* User home page, Where users can uppload a profile picture and write about thier experience in the art of mixology.
* Most popular carousel on the homepage where the most visited recepies over the last week can be displayed.
* Clone recipe button, that leads to a page similar to edit recepie, but instead saves as a new recepie, this would allow users to easily create their own version or a twist on a already existing cocktail.
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
* Tags, add tags that users can tag their recipes with to ease
* New recipes section where the latest recipes added are listed to give users looking to interact with active users a way to find the latest cocktails and comment on them.
* Improve comment section with threads that aRe minimized by default but can be expanded for any curious user.   

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
#### [TheCocktail DB api](https://www.thecocktaildb.com/)
The Ingredients and recipes collection on this site were built by calling the Cocktail db api, formating the appropriate information and insering the records into the database.

## Testing 
### Testing of user stories 


**Casual users:**  
This usergroup was seen as on that might visit the site, but not as frequently as the others. Therefor, to fullfill the userstories of a casual user, no login is required.  
* As a casual visitor I want to find a recepie so that I can try and make it.  
**Test:** Go to [https://the-cocktail-collection.herokuapp.com](https://the-cocktail-collection.herokuapp.com) find a new recipe.  
**Outcome:** The homepage features 30 recipes that can be tried aswell as e searchbar for further exploration. The user story is fullfilled, but could be further fullfilled by adding the previously mentioned Advanced search 
and Most popular features as well as randomizing the 30 recipes displayed on the Homepage.

* As a casual visitor I want to find a few recepies so that I can dazzle my guests with them in a upcoming party.  
**Test:** Go to [https://the-cocktail-collection.herokuapp.com](https://the-cocktail-collection.herokuapp.com) and find some recipes.
**Outcome:**The homepage features 30 recipes that can be tried aswell as e searchbar for further exploration. The user story is fullfilled, but could be further fullfilled by adding the previously mentioned Advanced search,
most popular, Print menu and print Bar-manual features as well as randomizing the 30 recipes displayed on the Homepage.  

**Enthusiast users:**  
The Enthusiast usergroup are seen as one that might frquent the site an therefore, to fullfill some of the userstories of enthusiasts, creating an account is required.
 If affiliate links to tools or glasses would be implemented, this usergroup is the main target.  
* As a Enthusiast visitor I want to find new recepie so that I can try it.
**Test:** Go to [https://the-cocktail-collection.herokuapp.com](https://the-cocktail-collection.herokuapp.com) find a new recipe.  
**Outcome:** The homepage features 30 recipes that can be tried aswell as e searchbar for further exploration. The user story is fullfilled, but could be further fullfilled by adding the previously mentioned Advanced search 
and Top list features as well as randomizing the 30 recipes displayed on the Homepage.  
* As a Enthusiast visitor I want to find new recepies so that I can try and make my own version of.  
**Test:** Go to [https://the-cocktail-collection.herokuapp.com](https://the-cocktail-collection.herokuapp.com) find a new recipe. To save the new recipe, go to [http://the-cocktail-collection.herokuapp.com/register](Register), sign up, log in, and the Create new recipe will be avliable in the navbar, there the new recipe can be created and saved.  
**Outcome:** The homepage features 30 recipes that can be tried aswell as e searchbar for further exploration. The user story is fullfilled, but could be further fullfilled by adding the previously mentioned Advanced search, 
Top list, Clone recipe, Collect recipe and User Homepage features as well as randomizing the 30 recipes displayed on the Homepage.  
* As a Enthusiast visitor I want to post my recepie so that I can get critique or tips from other users.
**Test:** Go to [https://the-cocktail-collection.herokuapp.com](https://the-cocktail-collection.herokuapp.com) after logging in Create new recipe. After the recipe has been created it can be searched for, seen, and commented on by all logged in users.  
**Outcome:** The create new recipe page adds any recipe created to the database and it can then be searched for in the searchbar and commented on by logged in users. The user story is fullfilled, but before a large enaugh userbase is established,
comments will be few and far appart. This userstory could be further fulfilled adding the previously mentioned New recipes section.  
* As a Enthusiast visitor I want to post my recepies so that I can save them for later use.
**Test:** Go to [https://the-cocktail-collection.herokuapp.com](https://the-cocktail-collection.herokuapp.com) after logging in Create new recipe. After the recipe has been created it can be searched for, seen, and commented on by all logged in users.  
**Outcome:** The create new recipe page adds any recipe created to the database and it can then be searched for in the searchbar and commented on by logged in users. The user story is fullfilled, but could be further fullfilled by adding the nefore mentioned user page where all recipies created by the users are avliable.  

**Professional users:**
The Professional usergroup are seen as one that might frquent the site an therefore, to fullfill some of the userstories of professionals, creating an account is required.  
* As a Professional user I want to find inspiration for a new cocktail so that I can put it on my menu.  
**Test:** Go to [https://the-cocktail-collection.herokuapp.com](https://the-cocktail-collection.herokuapp.com) find a new recipe.  
**Outcome:** The homepage features 30 recipes that can be tried aswell as e searchbar for further exploration. The user story is fullfilled, but could be further fullfilled by adding the previously mentioned Advanced search 
and New recipes section features so that trends in the community and new innovations more easily can be spotted.  
* As a Professional user I want to post my new recepie so that I can get some qritique before putting it on my menu.
**Test:** Go to [https://the-cocktail-collection.herokuapp.com](https://the-cocktail-collection.herokuapp.com) after logging in Create new recipe. After the recipe has been created it can be searched for, seen, and commented on by all logged in users.  
**Outcome:** The create new recipe page adds any recipe created to the database and it can then be searched for in the searchbar and commented on by logged in users. The user story is fullfilled, but before a large enaugh userbase is established,
comments will be few and far appart. This userstory could be further fulfilled adding the previously mentioned New recipes section.  
* As a Enthusiast visitor I want to post my recepies so that I can save them for later use.  

### Manual testing of site functionality
**Test:** Visit site and find recipe for Negroni using the searchbar.  
**Expected Outcome:** Landingpage displays, search shows recipe  for Negroni. Once Negroni is clicked, complete recipe displays.  
**Outcome:** Landingpage displays, search shows recipe  for Negroni. Once Negroni is clicked, complete recipe displays.  
**Passed:** Yes  

**Test:** Create new account and log in to it.  
**Expected Outcome:** Sign up form displays correctly and once submitted it is possible to sign in.  
**Outcome:** Sign up form displays correctly and once submitted it is possible to sign in.  
**Passed:** Yes  

**Test:** Create new recipe during recipe creation add incorect ingredient and remove it again.  
**Expected Outcome:** Form for creating recipe displays corectly and delete ingredient works once the recipe is submitted it is searcheable in the seachbar.  
**Outcome:** Form for creating recipe displays corectly and delete ingredient works once the recipe is submitted it is searcheable in the seachbar.  
**Passed:** Yes  

**Test:** Comment on the newly created recipe twice, delete one comment.  
**Expected Outcome:** Comments appears after being posted with visible delete button, and is removed when delete button is pressed.  
**Outcome:** Comments appears after being posted with visible delete button, and is removed when delete button is pressed.  
**Passed:** Yes  

**Test:** Delete recepie.  
**Expected Outcome:** Recipe is deleted from database and can no longer be found when searching.  
**Outcome:** Recipe is deleted from database and can no longer be found when searching.  
**Passed:** Yes  

**Test:** Try to delete, edit recipe and comments on a recipe created by another user.  
**Expected Outcome:** No delete or edit buttons avialble on the page.  
**Outcome:** No delete or edit buttons avialble on the page.  
**Passed:** Yes  

**Test:** Input empty fields in forms.  
**Expected Outcome:**  Browser asks for fields to be filled.  
**Outcome:**  Browser asks for fields to be filled.  
**Passed:** Yes  

**Test:** Sign out.  
**Expected Outcome:**  Session cookie is cleared and no account is logged in.   
**Outcome:**  Session cookie is cleared and no account is logged in.  
**Passed:** Yes  

**Test:** View on diferent sceen sizes and different browsers (Google Chrome, Mozilla Firefox, Safari, Microsoft edge).  
**Expected Outcome:**  Site behaves the same as in google chrome where it was developed.  
**Outcome:**  Site behaves the same as in google chrome where it was developed.  
**Passed:** Yes  


## Deployment 
## How to run this project locally.
* Make sure you have a IDE with a virtual enviroment running python3. Preferably gitpod online IDE.
This description will be based on you using Gitpod online IDE. 
* Go to [https://github.com/jourm/TheCocktailCollection](https://github.com/jourm/TheCocktailCollection) if you have Gitpod extension installed in you browser, a button with Gitpod will be visible next to clone/download press Gitpod.
* This will open the project in gitpod Online IDE. 
* Use pip to install all the required packages in requirements.txt 
* Register for an acount at https://www.mongodb.com/cloud/atlas. Create collections named: ingType, ingredients_new users and recepies(spelled incorectly, but unfortunatly mongo does not let collection names be changed once created.)
* Follow the MongoDB instructions for setting up connetion to your database( createing user, allowning network access)
* On the clusters page of you database, click connect > connect your application > select the latest version of python and copy the connection string.
* In your gitpod project create a new file called env.py import os and set os.environ["MONGO_URI"] = your connection string, make sure to replace <password> with your password.
* Add os.environ["SECRET"] = a random string of letters and numbers to env.py
* Run files in this order: dbbuilder.py, cocktaildbbuilder.py and finally create_dbindex.py, to populate ingType collection, ingredients_new collection, recepies collection and create a text searceable index for recepies collection.
* Run app.py and click open ports and open in browser to se the running project.

## Deploy on heroku.
* First follow steps to run project locally.
* Commit and push project to your github account.
* Create Heroku account.
* Create new app.
* On heroku, go to deploy > connect to github repo and connect heroku to you github repo.
* Settings > set config vars and set MONGO_URI and SECRET to the strings in your env.py, Set IP to 0.0.0.0 and PORT to 5000.
* Go to deploy, scroll down and click "enable automatic deploys"
