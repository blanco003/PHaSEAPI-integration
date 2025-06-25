import service.bot.PhaseApi as api
import dto.User as ud

# FOOD INFO

def get_valid_user_data():
    return ud.User("Test", 0, "Giacomo", "Rossi", "01/01/1990", "Italy", "english",[], [],[], [], False, 2, 12, "", [])


userData = get_valid_user_data()


food_info_recipe = "Lasagna"
recipe = api.get_information(food_info_recipe)
recipe.display()


# REC

mealDataJson = '''
{
  "mealType": "lunch",
  "ingredients_desired": ["zucchini", "chicken breast", "rice"],
  "ingredients_not_desired": ["mushrooms", "blue cheese"],
  "previous_recommendations": ["Grilled Chicken Bowl", "Veggie Stir Fry"]
}
'''


recipe = api.get_recipe_suggestion(mealDataJson, userData)
recipe.display()


# ALTERNATIVE

food_alternative = "Lasagna"
num_alternative = 3
base, imp = api.get_alternative(food_alternative, num_alternative, "overall")
print("\n###### BASE :")
recipe.display()
print("\n###### IMP :")
imp.display()


#################################################################################################################################################################

# FOOD INFO RECIPE

"""
Food info for 'Amatriciana': 200

{   
    'food_item': 'Capellini Amatriciana',
    'food_item_type': 'recipe',
    'healthiness': {
                    'score': 'D',
                    'qualitative': 'Poor healthiness level'},
    'sustainability': {'
                    score': 'A',
                    'qualitative': 'Excellent sustainability level',
                    'CF': 1.7655555555555558,
                    'WF': 2619.277777777778},
    'nutritional_values': {
                    'protein [g]': 13.2,
                    'calories [cal]': 376.5,
                    'caloriesFromFat [cal]': 42.0,
                    'totalFat [g]': 4.7,
                    'saturatedFat [g]': 1.2,
                    'cholesterol [mg]': 3.3,
                    'sodium [mg]': 374.2,
                    'totalCarbohydrate [g]': 68.6,
                    'dietaryFiber [g]': 5.2,
                    'sugars [g]': 9.5,
                    'duration': 30.0},
     'ingredients': {
                    'ingredients': ['capellini or 10 ounces spaghettini', 'olive oil', 'onions, coarsely chopped', 'garlic cloves, minced', 'dry white wine', 'no-salt-added whole tomatoes, drained and chopped, juices reserved', 'red pepper flakes', 'finely diced Canadian bacon', 'salt', 'minced fresh basil', 'grated parmesan cheese'],
                    'quantities': ['10  time(s) ounces ', '2  time(s) teaspoons ', '2  time(s) ', '2  time(s) ', '0.25 time(s) cup ', '1 time(s) (28 ounce) can ', '0.25 time(s) teaspoon ', '0.5 time(s) cup ', '0.5 time(s) teaspoon ', '3  time(s) tablespoons ', '3  time(s) tablespoons ']}
}


"""


#################################################################################################################################################################

# FOOD INFO INGREDIENT

# test_food_info("Onion")


"""
Food info for 'Onion': 200

{  
   'food_item': 'onion',
   'food_item_type': 'ingredient',
   'healthiness': None,
   'sustainability': {
                    'score': 'A',
                    'qualitative': 'Excellent sustainability level',
                    'CF': 0.33, 
                    'WF': 336.0}, 
    'nutritional_values': None, 
    'ingredients': None
}
"""


#################################################################################################################################################################

# ALTERNATIVE

"""
{
  "matched_food_item": {
    "food_item": "Spaghetti Carbonara",
    "food_item_type": "recipe",
    "healthiness": {
      "qualitative": "Good healthiness level",
      "score": "B"
    },
    "ingredients": {
      "ingredients": ["pasta","eggs","cheese pecorino","black pepper"],
      "quantities": ["100g","2","50g","to taste"]
    },
    "nutritional_values": {
      "calories [cal]": 450,
      "carbs [g]": 56,
      "fat [g]": 18,
      "protein [g]": 12
    },
    "sustainability": {
      "CF": 0.5,
      "WF": 0.3,
      "qualitative": "Inadequate sustainability level",
      "score": "E"
    }
  },
  "alternatives": [
    {
      "food_item": "Pasta alla gricia",
      "food_item_type": "recipe",
      "healthiness": {
        "qualitative": "Excellent healthiness level",
        "score": "A"
      },
      "ingredients": {
        "ingredients": ["pasta","guanciale","cheese pecorino","black pepper"],
        "quantities": ["100g","50g","30g","to taste"]
      },
      "nutritional_values": {
        "calories [cal]": 400,
        "carbs [g]": 50,
        "fat [g]": 10,
        "protein [g]": 15
      },
      "sustainability": {
        "CF": 0.5,
        "WF": 0.3,
        "qualitative": "Inadequate sustainability level",
        "score": "E"
      }
    },
    {
      "food_item": "Fettuccine Alfredo",
      "food_item_type": "recipe",
      "healthiness": {
        "qualitative": "Fair healthiness level",
        "score": "C"
      },
      "ingredients": {
        "ingredients": ["fettuccine","cream","parmesan cheese","butter"],
        "quantities": ["100g","50ml","30g","20g"]
      },
      "nutritional_values": {
        "calories [cal]": 500,
        "carbs [g]": 60,
        "fat [g]": 20,
        "protein [g]": 10
      },
      "sustainability": {
        "qualitative": "Good sustainability level",
        "score": "B"
      }
    },
    {
      "food_item": "Penne with basil pesto",
      "food_item_type": "recipe",
      "healthiness": {
        "qualitative": "Good healthiness level",
        "score": "B"
      },
      "ingredients": {
        "ingredients": ["penne","basil pesto", "olive oil","parmesan cheese"],
        "quantities": ["100g","30g","10ml","20g"]
      },
      "nutritional_values": {
        "calories [cal]": 480,
        "carbs [g]": 55,
        "fat [g]": 22,
        "protein [g]": 8
      },
      "sustainability": {
        "qualitative": "Fair sustainability level",
        "score": "C"
      }
    }
  ],
  "scores": [ 0.85, 0.75, 0.65]
}
"""

#################################################################################################################################################################

# RECOMMEND

"""
Recommendation: 500
Internal Server Error
"""

# dovrebbe rispondere con 
"""
{
  "user_id": 12345,
  "recommendations": [
    {
      "food_item": "Spaghetti Carbonara",
      "score": 0.92,
      "explanation": "U25 interacted_with 'Pasta amatriciana' has_ingredient 'guanciale' has_ingredient 'Spaghetti Carbonara'",
      "food_info": {
        "food_item": "Spaghetti Carbonara",
        "food_item_type": "recipe",
        "healthiness": {
          "qualitative": "Moderate healthiness level",
          "score": "B"
        },
        "sustainability": {
          "CF": 0.5,
          "WF": 0.3,
          "qualitative": "Moderate sustainability level",
          "score": "C"
        },
        "nutritional_values": {
          "calories [cal]": 450,
          "carbs [g]": 56,
          "fat [g]": 18,
          "protein [g]": 12
        },
        "ingredients": {
          "ingredients": [
            "pasta",
            "eggs",
            "cheese pecorino",
            "black pepper"
          ],
          "quantities": [
            "100g",
            "2",
            "50g",
            "to taste"
          ]
        }
      }
    }
  ],
  "conversation_id": "conv_2025032012345"
}
"""

#################################################################################################################################################################
