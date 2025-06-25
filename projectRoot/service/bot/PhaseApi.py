import json
import requests

import dto.Recipe as rp
import dto.Ingredient as ig
from service.domain import FoodHistoryService as fs


HEADER = {"Content-Type": "application/json"}
URL_RECCOMENDATION = "http://localhost:8100/recommend"
URL_INFORMATION = "http://localhost:8100/food-info/"
URL_ALTERNATIVE = "http://localhost:8100/alternative/"


def get_recipe_suggestion(mealDataJson, userData):
    
    # PRONTA MA NON FUNZIONA L'API
    
    """
    Parametri chiamata : 
      user_id : Unique identifier for the user
      preferences : List of food items, ingredients, or cuisines the user likes
      soft_restrictions : List of food items, ingredients, or cuisines the user dislikes
      hard_restrictions : List of specific food items to completely exclude from recommendations
      meal_time : What meal the user is looking for (breakfast, lunch, dinner, snack)
      previous_recommendations : List of previously recommended items to avoid repetition
      recommendation_count : Number of recommendations to return
      diversity_factor : Controls how diverse the recommendations should be (0.0-1.0)
      conversation_id : Identifier for the conversation these recommendations are associated with
    """
    


    
    if isinstance(mealDataJson, str):
      mealData = json.loads(mealDataJson)
    else:
      mealData = mealDataJson


    # recupera dal db la lista dei nomi delle ricette che l'utente ha consumato
    
    previous_recommendations = fs.get_consumed_recipes(userData.id)
    
    payload = {
        "user_id": userData.id,
        "preferences": mealData['ingredients_desired'],
        "soft_restrictions": mealData['ingredients_not_desired'],
        "hard_restrictions": userData.allergies,
        "meal_time": mealData['mealType'],
        "previous_recommendations": previous_recommendations,
        "recommendation_count": 1,
        "diversity_factor": 0.5,
        "conversation_id": userData.id
    }
    
    print("Payload : \n",payload)

    try :


      #response = requests.post(URL_RECCOMENDATION, headers=HEADER, json=payload)
      

      response_json = {
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

      #print(f"Status Code: {response.status_code}")
      print("Response JSON:", response_json)

      # estrazione prima ricetta suggerita e popolamento oggetto Recipe
      first_recipe_reccomended_dict = response_json["recommendations"][0]

      first_recipe_reccomended = rp.Recipe("", "", [], "", "", {})
      first_recipe_reccomended.from_recommendation_dict(first_recipe_reccomended_dict)


      return first_recipe_reccomended



    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta di raccomandazione all'utente {userData.id}:", e)
        return None
  



def get_food_info(item):
   
   try :
      response = requests.get(URL_INFORMATION + item, headers=HEADER)
      response_json = response.json()
      print(f"Status Code: {response.status_code}")
      print("Response JSON:", response_json)
      
       
      # l'endpoint è lo stesso per ricette e ingredienti, ma cambia il campo food_item_type della riposta
      if response_json["food_item_type"]=="recipe":
          recipe_information = rp.Recipe("", "", [], None, None, {})
          recipe_information.from_foodinfo_dict(response_json)
          return recipe_information

      else:
          ingredient_information = ig.Ingredient("", [], None, None, {})
          ingredient_information.from_food_info_dict(response_json)
          return ingredient_information
     
   except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta di recupero informazioni {item} :", e)
        return None




def get_alternative(recipe_name, num_alternative=5, improving_factor="overall"):
   
   try :
      
      payload = {
            "food_item": recipe_name,
            "num_alternatives": num_alternative
      }

      response = requests.post(URL_ALTERNATIVE, headers=HEADER, params=payload)
      response_json = response.json()

      print(f"Status Code: {response.status_code}")
      print("Response JSON:", response_json)



      # ricetta base che ha fatto il match
      base_recipe_dict = response_json["matched_food_item"]

      base_recipe = rp.Recipe("", "", [], None, None, {})
      base_recipe.from_alternative_dict(base_recipe_dict)
      #base_recipe.display()


      if improving_factor=="overall":
         # estrae semplicemente la prima suggerita
        imp_recipe_dict = response_json["alternatives"][0]

        imp_recipe = rp.Recipe("", "", [], None, None, {})
        imp_recipe.from_alternative_dict(imp_recipe_dict)
        #imp_recipe.display()

      else :
        
        # estrae la ricetta con miglior score di improving_factor rispetto a quello della ricetta che ha matchato
        base_score = base_recipe_dict.get(improving_factor, {}).get("score", "E")
        print(f"base recipe {improving_factor} score: {base_score}")

        # ordina le alternative dalla migliore alla peggiore
        sorted_alts = sorted(
             response_json["alternatives"],
             key=lambda alt: alt.get(improving_factor, {}).get("score", "E")
        )

        # trova la prima alternativa che ha score < base_score (cioè migliore)
        imp_recipe_dict = None
        for alt in sorted_alts:
            # recupero score ricetta temporanea
            alt_score = alt.get(improving_factor, {}).get("score", "E")
            if alt_score < base_score: 
                imp_recipe_dict = alt
                break

        # se nessuna alternativa è migliore, prendi la prima comunque
        if imp_recipe_dict is None:
             imp_recipe_dict = response_json["alternatives"][0]

        imp_recipe = rp.Recipe("", "", [], None, None, {})
        imp_recipe.from_alternative_dict(imp_recipe_dict)


      return base_recipe, imp_recipe
      
    
   except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta di alternative {recipe_name} :", e)
        return None

