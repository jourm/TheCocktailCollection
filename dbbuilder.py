import requests
import json


def getnewingredient(id):
    response = requests.get(
        'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid='
        + str(id))

    for value in response.json().values():

        return{"ingredient": value[0]['strIngredient'],
               "description": value[0]['strDescription'],
               "type": value[0]['strType'],
               "alcohol": value[0]['strAlcohol'],
               "abv": value[0]['strABV']}

