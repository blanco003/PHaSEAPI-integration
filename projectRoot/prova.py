import service.bot.PhaseApi as api
import dto.User as ud



##################################################################################################################################
# FOOD INFO

"""
food_info_recipe = "Lasagna"
recipe = api.get_food_info(food_info_recipe)
recipe.display()
"""

##################################################################################################################################
# RECOMMEND

"""
def get_valid_user_data():
    return ud.User("Test", 0, "Giacomo", "Rossi", "01/01/1990", "Italy", "english",[], [],[], [], False, 2, 12, "", [])


userData = get_valid_user_data()
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
"""



##################################################################################################################################
# ALTERNATIVE

"""
food_alternative = "Crispy Chicken Dijon"
num_alternative = 5
base_recipe, base_ing_info, imp_recipe, imp_ing_info = api.get_alternative(food_alternative, num_alternative, "sustainability")
print("\n###### BASE :")
base_recipe.display()
print("\n###### IMP :")
imp_recipe.display()


print("\n###### BASE ING INFO :\n")
for ing in base_ing_info:
  ing.display()
print("\n###### IMP ING INFO :\n")
for ing in imp_ing_info:
  ing.display()
"""




#################################################################################################################################################################
#################################################################################################################################################################

# ESEMPI


## FOOD INFO INGREDIENT

"""
...............................................................................

Calling http://localhost:8100/food-info/chicken

Status Code: 200
Response JSON: 

{ 
  'food_item': 'chicken',
  'food_item_type': 'ingredient', 
  'healthiness': None, 
  'sustainability': {
        'score': 'B', 
        'qualitative': 'Good sustainability level', 
        'CF': 3.88, 
        'WF': 4325.0},
  'nutritional_values': None, 
  'ingredients': None, 
  'food_item_url': None
}


...............................................................................

------------------------------------------------------------------------------------------

Name : chicken

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 3.88
  • WF: 4325.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------
"""

## FOOD INFO RECIPE


"""
...............................................................................

Calling http://localhost:8100/food-info/Lasagna

Status Code: 200
Response JSON: 

{
  'food_item': 'Lasagna', 
  'food_item_type': 'recipe', 
  'healthiness': {
        'score': 'D', 
        'qualitative': 'Poor healthiness level'}, 
  'sustainability': {
        'score': 'B', 
        'qualitative': 'Good sustainability level', 
        'CF': 3.501666666666667, 
        'WF': 4341.860576923077}, 
  'nutritional_values': {
        'protein [g]': 31.6, 
        'calories [cal]': 402.3, 
        'caloriesFromFat [cal]': 154.0, 
        'totalFat [g]': 17.2, 
        'saturatedFat [g]': 8.3, 
        'cholesterol [mg]': 96.7, 
        'sodium [mg]': 939.6, 
        'totalCarbohydrate [g]': 29.7, 
        'dietaryFiber [g]': 2.4, 
        'sugars [g]': 6.8, 
        'duration': 80.0}, 
  'ingredients': {
        'ingredients': ['lasagna noodles', 'lean ground beef', 'tomato sauce', 'green pepper, chopped fine', 'onions, chopped fine', 'sugar', 'garlic salt', 'oregano', 'pepper, to taste', 'cottage cheese', 'parmesan cheese, grated', 'egg', 'parsley flakes', 'pepper, to taste', 'mozzarella cheese, grated'], 
        'quantities': ['10 -12  time(s) ', '1  time(s) lb ', '640  time(s) ml ', '0.25 time(s) cup ', '2  time(s) tablespoons ', '1  time(s) teaspoon ', '1  time(s) teaspoon ', '0.5 time(s) teaspoon ', ' time(s) ', '2  time(s) cups ', '0.5 time(s) cup ', '1 time(s) ', '1  time(s) tablespoon ', ' time(s) ', '2  time(s) cups ']}, 
  'food_item_url': None
}

...............................................................................

------------------------------------------------------------------------------------------

Name : Lasagna
Spiegazione:

Healthiness Score: D
  • Qualitative: Poor healthiness level

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 3.501666666666667
  • WF: 4341.860576923077

Ingredienti:
  - lasagna noodles: 10 -12  time(s)
  - lean ground beef: 1  time(s) lb
  - tomato sauce: 640  time(s) ml
  - green pepper, chopped fine: 0.25 time(s) cup
  - onions, chopped fine: 2  time(s) tablespoons
  - sugar: 1  time(s) teaspoon
  - garlic salt: 1  time(s) teaspoon
  - oregano: 0.5 time(s) teaspoon
  - pepper, to taste:  time(s)
  - cottage cheese: 2  time(s) cups
  - parmesan cheese, grated: 0.5 time(s) cup
  - egg: 1 time(s)
  - parsley flakes: 1  time(s) tablespoon
  - pepper, to taste:  time(s)
  - mozzarella cheese, grated: 2  time(s) cups

Valori nutrizionali:
  • protein [g]: 31.6
  • calories [cal]: 402.3
  • caloriesFromFat [cal]: 154.0
  • totalFat [g]: 17.2
  • saturatedFat [g]: 8.3
  • cholesterol [mg]: 96.7
  • sodium [mg]: 939.6
  • totalCarbohydrate [g]: 29.7
  • dietaryFiber [g]: 2.4
  • sugars [g]: 6.8
  • duration: 80.0

URL : None
------------------------------------------------------------------------------------------
"""


## RECOMMEND : DUMMY
"""
...............................................................................

Calling /recommend with payload:
{'user_id': '0', 'preferences': ['zucchini', 'chicken breast', 'rice'], 'soft_restrictions': ['mushrooms', 'blue cheese'], 'hard_restrictions': [], 'meal_time': 'lunch', 'previous_recommendations': None, 'recommendation_count': 3, 'diversity_factor': 0.5, 'conversation_id': '0'}
Response JSON: {'user_id': 12345, 'recommendations': [{'food_item': 'Spaghetti Carbonara', 'score': 0.92, 'explanation': "U25 interacted_with 'Pasta amatriciana' has_ingredient 'guanciale' has_ingredient 'Spaghetti Carbonara'", 'food_info': {'food_item': 'Spaghetti Carbonara', 'food_item_type': 'recipe', 'food_item_url': 'https://www.food.com/recipe/spaghetti-carbonara-for-one-447544', 'healthiness': {'qualitative': 'Moderate healthiness level', 'score': 'B'}, 'sustainability': {'CF': 0.5, 'WF': 0.3, 'qualitative': 'Moderate sustainability level', 'score': 'C'}, 'nutritional_values': {'calories [cal]': 450, 'carbs [g]': 56, 'fat [g]': 18, 'protein [g]': 12}, 'ingredients': {'ingredients': ['pasta', 'eggs', 'cheese pecorino', 'black pepper'], 'quantities': ['100g', '2', '50g', 'to taste']}}}], 'conversation_id': 'conv_2025032012345'}

...............................................................................

------------------------------------------------------------------------------------------

Name : Spaghetti Carbonara
Spiegazione: U25 interacted_with 'Pasta amatriciana' has_ingredient 'guanciale' has_ingredient 'Spaghetti Carbonara' 

Healthiness Score: B
  • Qualitative: Moderate healthiness level

Sustainability Score: C
  • Qualitative: Moderate sustainability level
  • CF: 0.5
  • WF: 0.3

Ingredienti:
  - pasta: 100g
  - eggs: 2
  - cheese pecorino: 50g
  - black pepper: to taste

Valori nutrizionali:
  • calories [cal]: 450.0
  • carbs [g]: 56.0
  • fat [g]: 18.0
  • protein [g]: 12.0

URL : https://www.food.com/recipe/spaghetti-carbonara-for-one-447544
------------------------------------------------------------------------------------------
"""


## ALTERNATIVE

"""

food_alternative = "Crispy Chicken Dijon"
num_alternative = 5
base_recipe, base_ing_info, imp_recipe, imp_ing_info = api.get_alternative(food_alternative, num_alternative, "sustainability")


...............................................................................

Calling /alternative with payload:
{'food_item': 'Crispy Chicken Dijon', 'num_alternatives': 5}

Status Code: 200
Response JSON: {'matched_food_item': {'food_item': 'Crispy Chicken Dijon', 'food_item_type': 'recipe', 'healthiness': {'score': 'D', 'qualitative': 'Poor healthiness level'}, 'sustainability': {'score': 'E', 'qualitative': 'Inadequate sustainability level', 'CF': 0.7764285714285714, 'WF': 22241.571428571428}, 'nutritional_values': {'protein [g]': 39.6, 'calories [cal]': 656.7, 'caloriesFromFat [cal]': 266.0, 'totalFat [g]': 29.6, 'saturatedFat [g]': 3.1, 'cholesterol [mg]': 71.1, 'sodium [mg]': 1360.8, 'totalCarbohydrate [g]': 58.2, 'dietaryFiber [g]': 8.8, 'sugars [g]': 6.1, 'duration': 45.0}, 'ingredients': {'ingredients': ['chickpeas, drained and rinsed', 'cherry tomatoes, halved', 'red onion, chopped (small, about 1 cup)', 'canola oil', 'salt', 'pepper', 'lemon juice', 'plain yogurt', 'Dijon mustard', 'garlic clove, minced', 'boneless skinless chicken breasts', 'breadcrumbs (preferably panko)', 'canola oil, divided', 'salt', 'pepper'], 'quantities': ['1 time(s) (540 ml) can ', '2  time(s) cups ', '1  time(s) ', '3  time(s) tablespoons ', '0.5 time(s) teaspoon ', '0.25 time(s) teaspoon ', '1  time(s) tablespoon ', '0.3333333333333333 time(s) cup ', '2  time(s) tablespoons ', '1  time(s) ', '4  time(s) ', '1  time(s) cup ', '0.25 time(s) cup ', '0.5 time(s) teaspoon ', '0.25 time(s) teaspoon ']}, 'food_item_url': 'https://www.food.com/recipe/crispy-chicken-dijon-413295'}, 'alternatives': [{'food_item': 'Crispy Dijon Chicken', 'food_item_type': 'recipe', 'healthiness': {'score': 'D', 'qualitative': 'Poor healthiness level'}, 'sustainability': {'score': 'C', 'qualitative': 'Fair sustainability level', 'CF': 2.396666666666667, 'WF': 5206.0}, 'nutritional_values': {'protein [g]': 29.0, 'calories [cal]': 198.6, 'caloriesFromFat [cal]': 52.0, 'totalFat [g]': 5.8, 'saturatedFat [g]': 1.9, 'cholesterol [mg]': 81.0, 'sodium [mg]': 458.5, 'totalCarbohydrate [g]': 5.9, 'dietaryFiber [g]': 0.8, 'sugars [g]': 0.6, 'duration': 35.0}, 'ingredients': {'ingredients': ['boneless skinless chicken breast halves', 'Dijon mustard', 'fat-free evaporated milk', 'dry breadcrumbs', 'grated parmesan cheese'], 'quantities': ['4  time(s) ', '0.25 time(s) cup ', '0.25 time(s) ', '0.25 time(s) cup ', '0.25 time(s) cup ']}, 'food_item_url': 'https://www.food.com/recipe/crispy-dijon-chicken-125751'}, {'food_item': 'Crispy Dijon Chicken', 'food_item_type': 'recipe', 'healthiness': {'score': 'D', 'qualitative': 'Poor healthiness level'}, 'sustainability': {'score': 'C', 'qualitative': 'Fair sustainability level', 'CF': 2.396666666666667, 'WF': 5206.0}, 'nutritional_values': {'protein [g]': 29.0, 'calories [cal]': 198.6, 'caloriesFromFat [cal]': 52.0, 'totalFat [g]': 5.8, 'saturatedFat [g]': 1.9, 'cholesterol [mg]': 81.0, 'sodium [mg]': 458.5, 'totalCarbohydrate [g]': 5.9, 'dietaryFiber [g]': 0.8, 'sugars [g]': 0.6, 'duration': 35.0}, 'ingredients': {'ingredients': ['boneless skinless chicken breast halves', 'Dijon mustard', 'fat-free evaporated milk', 'dry breadcrumbs', 'grated parmesan cheese'], 'quantities': ['4  time(s) ', '0.25 time(s) cup ', '0.25 time(s) ', '0.25 time(s) cup ', '0.25 time(s) cup ']}, 'food_item_url': 'https://www.food.com/recipe/crispy-dijon-chicken-125751'}, {'food_item': 'Crunchy Crispy Chicken Dijon', 'food_item_type': 'recipe', 'healthiness': {'score': 'D', 'qualitative': 'Poor healthiness level'}, 'sustainability': {'score': 'B', 'qualitative': 'Good sustainability level', 'CF': 3.138, 'WF': 4341.860576923077}, 'nutritional_values': {'protein [g]': 35.0, 'calories [cal]': 342.0, 'caloriesFromFat [cal]': 125.0, 'totalFat [g]': 14.0, 'saturatedFat [g]': 2.3, 'cholesterol [mg]': 96.8, 'sodium [mg]': 307.4, 'totalCarbohydrate [g]': 16.8, 'dietaryFiber [g]': 0.9, 'sugars [g]': 1.1, 'duration': 30.0}, 'ingredients': {'ingredients': ['boneless skinless chicken breast', 'all-purpose flour', 'honey dijon mustard', 'dry breadcrumbs, plain', 'vegetable oil'], 'quantities': ['1  time(s) lb ', '2  time(s) tablespoons ', '5  time(s) tablespoons ', '0.5 time(s) cup ', '2  time(s) tablespoons ']}, 'food_item_url': 'https://www.food.com/recipe/crunchy-crispy-chicken-dijon-281060'}, {'food_item': 'Crispy Honey Dijon Chicken', 'food_item_type': 'recipe', 'healthiness': {'score': 'E', 'qualitative': 'Inadequate healthiness level'}, 'sustainability': {'score': 'B', 'qualitative': 'Good sustainability level', 'CF': 1.9209090909090911, 'WF': 4341.860576923077}, 'nutritional_values': {'protein [g]': 53.3, 'calories [cal]': 589.4, 'caloriesFromFat [cal]': 159.0, 'totalFat [g]': 17.8, 'saturatedFat [g]': 3.8, 'cholesterol [mg]': 145.3, 'sodium [mg]': 1511.2, 'totalCarbohydrate [g]': 53.6, 'dietaryFiber [g]': 2.5, 'sugars [g]': 27.1, 'duration': 45.0}, 'ingredients': {'ingredients': ['boneless skinless chicken breasts', 'Dijon mustard', 'honey', 'salt', 'pepper', 'Ritz crackers, crushed'], 'quantities': ['1 1/2 time(s) lbs ', '0.5 time(s) cup ', '0.25 time(s) cup ', '0.5 time(s) teaspoon ', '0.25 time(s) teaspoon ', '40 -50  time(s) ']}, 'food_item_url': 'https://www.food.com/recipe/crispy-honey-dijon-chicken-97168'}, {'food_item': 'Easy Crispy Dijon Chicken', 'food_item_type': 'recipe', 'healthiness': {'score': 'E', 'qualitative': 'Inadequate healthiness level'}, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 1.0799999999999998, 'WF': 2316.0}, 'nutritional_values': {'protein [g]': 31.8, 'calories [cal]': 347.8, 'caloriesFromFat [cal]': 185.0, 'totalFat [g]': 20.6, 'saturatedFat [g]': 11.3, 'cholesterol [mg]': 122.7, 'sodium [mg]': 613.4, 'totalCarbohydrate [g]': 7.8, 'dietaryFiber [g]': 0.7, 'sugars [g]': 0.3, 'duration': 50.0}, 'ingredients': {'ingredients': ['boneless skinless chicken breasts', 'butter (I use half)', 'Dijon mustard (or whatever mustard you like)', 'half-and-half (or whatever milk you have around)', 'cracker crumbs or 1/4 cup breadcrumbs, just use what you like', 'parmesan cheese or 1/2 cup $template2$'], 'quantities': ['4  time(s) ', '4  time(s) tablespoons ', '0.25 time(s) cup ', '0.25 time(s) cup ', '0.25 time(s) cup ', '0.5 time(s) cup ']}, 'food_item_url': 'https://www.food.com/recipe/easy-crispy-dijon-chicken-352692'}], 'scores': [0.9274316554268202, 0.9274316554268202, 1.242104043563207, 1.5588770747184755, 1.9071110546588896]}

base recipe sustainability score: E
improved recipe sustainability score: A

###############################################################################
base ingredients :  [('chickpeas, drained and rinsed', '1 time(s) (540 ml) can '), ('cherry tomatoes, halved', '2  time(s) cups '), ('red onion, chopped (small, about 1 cup)', '1  time(s) '), ('canola oil', '3  time(s) tablespoons '), ('salt', '0.5 time(s) teaspoon '), ('pepper', '0.25 time(s) teaspoon '), ('lemon juice', '1  time(s) tablespoon '), ('plain yogurt', '0.3333333333333333 time(s) cup '), ('Dijon mustard', '2  time(s) tablespoons '), ('garlic clove, minced', '1  time(s) '), ('boneless skinless chicken breasts', '4  time(s) '), ('breadcrumbs (preferably panko)', '1  time(s) cup '), ('canola oil, divided', '0.25 time(s) cup '), ('salt', '0.5 time(s) teaspoon '), ('pepper', '0.25 time(s) teaspoon ')]

improved ingredients :  [('boneless skinless chicken breasts', '4  time(s) '), ('butter (I use half)', '4  time(s) tablespoons '), ('Dijon mustard (or whatever mustard you like)', '0.25 time(s) cup '), ('half-and-half (or whatever milk you have around)', '0.25 time(s) cup '), ('cracker crumbs or 1/4 cup breadcrumbs, just use what you like', '0.25 time(s) cup '), ('parmesan cheese or 1/2 cup $template2$', '0.5 time(s) cup ')]

...............................................................................

Calling http://localhost:8100/food-info/chickpeas, drained and rinsed

Status Code: 200
Response JSON: {'food_item': 'Sauteed Chickpeas/Garbanzos', 'food_item_type': 'recipe', 'healthiness': {'score': 'C', 'qualitative': 'Fair healthiness level'}, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 2.776666666666667, 'WF': 2544.6666666666665}, 'nutritional_values': {'protein [g]': 11.1, 'calories [cal]': 363.5, 'caloriesFromFat [cal]': 115.0, 'totalFat [g]': 12.8, 'saturatedFat [g]': 1.7, 'cholesterol [mg]': 0.0, 'sodium [mg]': 1055.1, 'totalCarbohydrate [g]': 53.2, 'dietaryFiber [g]': 10.5, 'sugars [g]': 3.3, 'duration': 17.0}, 'ingredients': {'ingredients': ['olive oil', 'garbanzo beans, drained, reserving 1/2 cup of bean juice', 'onion, diced', 'cumin', 'chili powder', 'salt', 'diced tomato, drained, juice reserved'], 'quantities': ['3  time(s) tablespoons ', '1 time(s) (29 ounce) can ', '0.5 time(s) cup ', '1  time(s) teaspoon ', '1  time(s) teaspoon ', '0.5 time(s) teaspoon ', '1  time(s) cup ']}, 'food_item_url': None}

...............................................................................

Calling http://localhost:8100/food-info/cherry tomatoes, halved

Status Code: 200
Response JSON: {'food_item': 'cherry tomatoes', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 0.45, 'WF': 41.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : cherry tomatoes

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 0.45
  • WF: 41.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/red onion, chopped (small, about 1 cup)

Status Code: 200
Response JSON: {'food_item': 'red onion', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 0.33, 'WF': 336.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : red onion

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 0.33
  • WF: 336.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/canola oil

Status Code: 200
Response JSON: {'food_item': 'canola oil', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'B', 'qualitative': 'Good sustainability level', 'CF': 1.79, 'WF': 4301.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : canola oil

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 1.79
  • WF: 4301.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/salt

Status Code: 200
Response JSON: {'food_item': 'salt', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': None, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : salt

Healthiness Score: N/A

Sustainability Score: N/A

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/pepper

Status Code: 200
Response JSON: {'food_item': 'pepper', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'D', 'qualitative': 'Poor sustainability level', 'CF': 0.84, 'WF': 7611.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : pepper

Healthiness Score: N/A

Sustainability Score: D
  • Qualitative: Poor sustainability level
  • CF: 0.84
  • WF: 7611.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/lemon juice

Status Code: 200
Response JSON: {'food_item': 'lemon juice', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 2.86, 'WF': 1019.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : lemon juice

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 2.86
  • WF: 1019.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/plain yogurt

Status Code: 200
Response JSON: {'food_item': 'plain yogurt', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 1.69, 'WF': 1540.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : plain yogurt

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.69
  • WF: 1540.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/Dijon mustard

Status Code: 200
Response JSON: {'food_item': 'Dijon Mustard', 'food_item_type': 'recipe', 'healthiness': {'score': 'C', 'qualitative': 'Fair healthiness level'}, 'sustainability': {'score': 'B', 'qualitative': 'Good sustainability level', 'CF': 2.4254545454545458, 'WF': 4341.860576923077}, 'nutritional_values': {'protein [g]': 0.9, 'calories [cal]': 44.7, 'caloriesFromFat [cal]': 32.0, 'totalFat [g]': 3.6, 'saturatedFat [g]': 0.4, 'cholesterol [mg]': 1.9, 'sodium [mg]': 52.7, 'totalCarbohydrate [g]': 2.6, 'dietaryFiber [g]': 0.4, 'sugars [g]': 0.7, 'duration': 5.0}, 'ingredients': {'ingredients': ['dry mustard', 'water', 'white wine vinegar ((or 1/2 white wine, 1/2 white vinegar)', 'mayonnaise', 'pinch sugar'], 'quantities': ['1  time(s) tablespoon ', '1  time(s) teaspoon ', '1  time(s) teaspoon ', '1  time(s) tablespoon ', '1  time(s) ']}, 'food_item_url': None}

...............................................................................

Calling http://localhost:8100/food-info/garlic clove, minced

Status Code: 200
Response JSON: {'food_item': 'minced garlic clove', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 1.3, 'WF': 1378.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : minced garlic clove

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.3
  • WF: 1378.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/boneless skinless chicken breasts

Status Code: 200
Response JSON: {'food_item': 'boneless skinless chicken breasts', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'B', 'qualitative': 'Good sustainability level', 'CF': 3.68, 'WF': 3960.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : boneless skinless chicken breasts

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 3.68
  • WF: 3960.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/breadcrumbs (preferably panko)

Status Code: 200
Response JSON: {'food_item': 'panko breadcrumbs', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 0.57, 'WF': 2133.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : panko breadcrumbs

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 0.57
  • WF: 2133.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/canola oil, divided

Status Code: 200
Response JSON: {'food_item': 'canola oil', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'B', 'qualitative': 'Good sustainability level', 'CF': 1.79, 'WF': 4301.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : canola oil

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 1.79
  • WF: 4301.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/salt

Status Code: 200
Response JSON: {'food_item': 'salt', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': None, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : salt

Healthiness Score: N/A

Sustainability Score: N/A

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/pepper

Status Code: 200
Response JSON: {'food_item': 'pepper', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'D', 'qualitative': 'Poor sustainability level', 'CF': 0.84, 'WF': 7611.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : pepper

Healthiness Score: N/A

Sustainability Score: D
  • Qualitative: Poor sustainability level
  • CF: 0.84
  • WF: 7611.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/boneless skinless chicken breasts

Status Code: 200
Response JSON: {'food_item': 'boneless skinless chicken breasts', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'B', 'qualitative': 'Good sustainability level', 'CF': 3.68, 'WF': 3960.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : boneless skinless chicken breasts

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 3.68
  • WF: 3960.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/butter (I use half)

Status Code: 200
Response JSON: {'food_item': 'Butter', 'food_item_type': 'recipe', 'healthiness': {'score': 'E', 'qualitative': 'Inadequate healthiness level'}, 'sustainability': {'score': 'B', 'qualitative': 'Good sustainability level', 'CF': 1.4642857142857142, 'WF': 3542.714285714286}, 'nutritional_values': {'protein [g]': 4.9, 'calories [cal]': 821.1, 'caloriesFromFat [cal]': 792.0, 'totalFat [g]': 88.1, 'saturatedFat [g]': 54.8, 'cholesterol [mg]': 326.1, 'sodium [mg]': 90.4, 'totalCarbohydrate [g]': 6.6, 'dietaryFiber [g]': 0.0, 'sugars [g]': 0.3, 'duration': 315.0}, 'ingredients': {'ingredients': ['heavy cream', 'salt, if salted butter needed'], 'quantities': ['1  time(s) cup ', ' time(s) ']}, 'food_item_url': None}

...............................................................................

Calling http://localhost:8100/food-info/Dijon mustard (or whatever mustard you like)

Status Code: 200
Response JSON: {'food_item': 'dijon - style mustard', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 1.46, 'WF': 572.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : dijon - style mustard

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.46
  • WF: 572.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/half-and-half (or whatever milk you have around)

Status Code: 200
Response JSON: {'food_item': 'half and half milk', 'food_item_type': 'ingredient', 'healthiness': None, 'sustainability': {'score': 'A', 'qualitative': 'Excellent sustainability level', 'CF': 1.44, 'WF': 1599.0}, 'nutritional_values': None, 'ingredients': None, 'food_item_url': None}

...............................................................................

------------------------------------------------------------------------------------------

Name : half and half milk

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.44
  • WF: 1599.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

...............................................................................

Calling http://localhost:8100/food-info/cracker crumbs or 1/4 cup breadcrumbs, just use what you like

Status Code: 404
Non trovato!

...............................................................................

Calling http://localhost:8100/food-info/parmesan cheese or 1/2 cup $template2$

Status Code: 404
Non trovato!
###############################################################################

...............................................................................

###### BASE :

------------------------------------------------------------------------------------------

Name : Crispy Chicken Dijon
Spiegazione:

Healthiness Score: D
  • Qualitative: Poor healthiness level

Sustainability Score: E
  • Qualitative: Inadequate sustainability level
  • CF: 0.7764285714285714
  • WF: 22241.571428571428

Ingredienti:
  - chickpeas, drained and rinsed: 1 time(s) (540 ml) can
  - cherry tomatoes, halved: 2  time(s) cups
  - red onion, chopped (small, about 1 cup): 1  time(s)
  - canola oil: 3  time(s) tablespoons
  - salt: 0.5 time(s) teaspoon
  - pepper: 0.25 time(s) teaspoon
  - lemon juice: 1  time(s) tablespoon
  - plain yogurt: 0.3333333333333333 time(s) cup
  - Dijon mustard: 2  time(s) tablespoons
  - garlic clove, minced: 1  time(s)
  - boneless skinless chicken breasts: 4  time(s)
  - breadcrumbs (preferably panko): 1  time(s) cup
  - canola oil, divided: 0.25 time(s) cup
  - salt: 0.5 time(s) teaspoon
  - pepper: 0.25 time(s) teaspoon

Valori nutrizionali:
  • protein [g]: 39.6
  • calories [cal]: 656.7
  • caloriesFromFat [cal]: 266.0
  • totalFat [g]: 29.6
  • saturatedFat [g]: 3.1
  • cholesterol [mg]: 71.1
  • sodium [mg]: 1360.8
  • totalCarbohydrate [g]: 58.2
  • dietaryFiber [g]: 8.8
  • sugars [g]: 6.1
  • duration: 45.0

URL : https://www.food.com/recipe/crispy-chicken-dijon-413295
------------------------------------------------------------------------------------------

###### IMP :

------------------------------------------------------------------------------------------

Name : Easy Crispy Dijon Chicken
Spiegazione:

Healthiness Score: E
  • Qualitative: Inadequate healthiness level

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.0799999999999998
  • WF: 2316.0

Ingredienti:
  - boneless skinless chicken breasts: 4  time(s)
  - butter (I use half): 4  time(s) tablespoons
  - Dijon mustard (or whatever mustard you like): 0.25 time(s) cup
  - half-and-half (or whatever milk you have around): 0.25 time(s) cup
  - cracker crumbs or 1/4 cup breadcrumbs, just use what you like: 0.25 time(s) cup
  - parmesan cheese or 1/2 cup $template2$: 0.5 time(s) cup

Valori nutrizionali:
  • protein [g]: 31.8
  • calories [cal]: 347.8
  • caloriesFromFat [cal]: 185.0
  • totalFat [g]: 20.6
  • saturatedFat [g]: 11.3
  • cholesterol [mg]: 122.7
  • sodium [mg]: 613.4
  • totalCarbohydrate [g]: 7.8
  • dietaryFiber [g]: 0.7
  • sugars [g]: 0.3
  • duration: 50.0

URL : https://www.food.com/recipe/easy-crispy-dijon-chicken-352692
------------------------------------------------------------------------------------------

###### BASE ING INFO :


------------------------------------------------------------------------------------------

Name : cherry tomatoes

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 0.45
  • WF: 41.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : red onion

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 0.33
  • WF: 336.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : canola oil

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 1.79
  • WF: 4301.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : salt

Healthiness Score: N/A

Sustainability Score: N/A

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : pepper

Healthiness Score: N/A

Sustainability Score: D
  • Qualitative: Poor sustainability level
  • CF: 0.84
  • WF: 7611.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : lemon juice

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 2.86
  • WF: 1019.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : plain yogurt

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.69
  • WF: 1540.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : minced garlic clove

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.3
  • WF: 1378.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : boneless skinless chicken breasts

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 3.68
  • WF: 3960.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : panko breadcrumbs

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 0.57
  • WF: 2133.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : canola oil

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 1.79
  • WF: 4301.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : salt

Healthiness Score: N/A

Sustainability Score: N/A

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : pepper

Healthiness Score: N/A

Sustainability Score: D
  • Qualitative: Poor sustainability level
  • CF: 0.84
  • WF: 7611.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

###### IMP ING INFO :


------------------------------------------------------------------------------------------

Name : boneless skinless chicken breasts

Healthiness Score: N/A

Sustainability Score: B
  • Qualitative: Good sustainability level
  • CF: 3.68
  • WF: 3960.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------

Name : dijon - style mustard

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.46
  • WF: 572.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------
Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.46
  • WF: 572.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------
Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.46
  • WF: 572.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------
  • CF: 1.46
  • WF: 572.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------
Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------

Name : half and half milk

Healthiness Score: N/A

Sustainability Score: A
  • Qualitative: Excellent sustainability level
  • CF: 1.44
  • WF: 1599.0

Ingredients: N/A

Nutritional Values:

URL : None
------------------------------------------------------------------------------------------
"""
