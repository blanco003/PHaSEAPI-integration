import math

import jsonpickle
import service.domain.IngredientService as ingredientService
import dto.Recipe as recipe



def compute_normalized_cfp_sustainability(ingredients):
    """
    Calcola il carbon footprint normalizzato di una lista di ingredienti, istanze della classe Ingredient.

    Args 
    - ingredients : lista di ingredienti, istanze della classe Ingredient, di cui calcolare il cfp normalizzato.

    Returns : 
    - cfP_score : carbon footprint normalizzato della data lista di ingredienti.
    """
    normalized_cfps = []
    max_cfp = 78.8
    for ingredient in ingredients:
        if(ingredient.cfp != None):
            normalized_cfps.append(ingredient.cfp/max_cfp)
    #order cfps in descending order
    normalized_cfps.sort(reverse=True)

    cfp_score = 0
    for i in range(len(normalized_cfps)):
        cfp_score += normalized_cfps[i] * math.e ** (-i)
    
    return cfp_score

def compute_normalized_wfp_sustainability(ingredients):
    """
    Calcola il water footprint normalizzato di una lista di ingredienti, istanze della classe Ingredient.

    Args 
    - ingredients : lista di ingredienti, istanze della classe Ingredient, di cui calcolare il wfp normalizzato.

    Returns : 
    - wfP_score : carbon footprint normalizzato della data lista di ingredienti.
    """
    normalized_wfps = []
    max_wfp = 731000
    for ingredient in ingredients:
        if(ingredient.wfp != None):
            normalized_wfps.append(ingredient.wfp/max_wfp)
    #order wfps in descending order
    normalized_wfps.sort(reverse=True)

    wfp_score = 0
    for i in range(len(normalized_wfps)):
        wfp_score += normalized_wfps[i] * math.e ** (-i)
    
    return wfp_score


def compute_recipe_sustainability_score(recipe):
    """
    Calcola lo score di sostenibilità di una ricetta, come combinazione lineare del carbon footprint e water footprint,
    degli ingredienti contentuti nella ricetta, istanza della classe Recipe.

    Args : 
    - recipe : ricetta di cui calcolare lo score di sostenibilità.
    """

    # ingredients non è più una lista di oggetti di classe Ingredient
    # ma un dizionario contenente i campi ingredients e quantities
    
    ingredient_names = recipe.ingredients.get("ingredients", []) 

    ingredients = []
    #ingredients = recipe.ingredients

    for ingredient in ingredient_names:
        ing_obj = ingredientPersistence.get_most_similar_ingredient(ingredient)
        ingredients.append(ing_obj)
    
    

    alpha = 0.8
    beta = 0.2
    max_overall_sustainability = 0.8689
    cfp_score = compute_normalized_cfp_sustainability(ingredients)
    wfp_score = compute_normalized_wfp_sustainability(ingredients)

    overall_sustainability = alpha * cfp_score + beta * wfp_score
    normalized_overall_sustainability = overall_sustainability / max_overall_sustainability
    recipe.sustainability_score = normalized_overall_sustainability


def get_recipe_cluster(recipe):
    """
    Assegna alla ricetta il cluster di sostenibilità, in base al suo score di sostenibilità, in particolare . 
    - 0 : se lo score di sostenibilità appartiene all'intervallo [0, 0.04]
    - 1 : se lo score di sostenibilità appartiene all'intervallo ]0.04, 0.15]
    - 2 : se lo score di sostenibilità appartiene all'intervallo ]0.15, 1]
    
    Args : 
    - recipe : ricetta di cui calcolare l'indice del cluster di sostenibilità.

    Returns : 
    - int : indice del cluster di sostenibilità assegnato alla ricetta.
    """

    #if the sustainability score is in [0, 0.04] then the recipe belongs to cluster 0
    if recipe.sustainability_score >= 0 and recipe.sustainability_score <= 0.04:
        return 0
    
    #if the sustainability score is in ]0.04, 0.15] then the recipe belongs to cluster 1
    if recipe.sustainability_score > 0.04 and recipe.sustainability_score <= 0.15:
        return 1
    
    #if the sustainability score is in ]0.15, 1] then the recipe belongs to cluster 2
    if recipe.sustainability_score > 0.15 and recipe.sustainability_score <= 1:
        return 2


def convert_in_emealio_recipe(mongoRecipe,removedConstraints,mealType):
    """
    Converte una ricetta nel formato del mongodb (dizionario) in un oggetto istanza
    della classe Recipe, utilizzabile dal sistema E-malio.

    Args : 
    - mongoRecipe : ricetta nel formato mongodb.
    - removedConstraints : vincoli rimossi per poter estrarre la ricetta dal db.
    - mealType : tipologia di pasto della ricetta.

    Retursn :
    - Recipe : ricetta sotto forma di oggetto istanza della classe Recipe rappresentante la ricetta nel formato mongodb.
    """
    title = mongoRecipe['title']
    id = mongoRecipe['recipe_id']
    instructions = mongoRecipe['recipe_url']
    sustainabilityScore = mongoRecipe['sustainability_score']
    who_score = mongoRecipe['who_score']
    #check if the description is present
    if 'description' in mongoRecipe:
        description = mongoRecipe['description']
    else:
        description = None
    ingredients = ingredientService.get_ingredient_list_from_full_ingredient_string(mongoRecipe['ingredients'])
    return recipe.Recipe(title,id,ingredients,sustainabilityScore,who_score,instructions,description,removedConstraints,mealType)


def get_substitutions_info(DataJson):
    """
    Estre da una stringa JSON le informazioni contentute riguardo a eventuali ingredienti da rimuovere/aggiungere
    in una ricetta.
    
    Args : 
    - DataJson : stringa JSON
    
    Returns :
    - ingredients_to_remove, ingredients_to_add : eventuali informazioni codificate nella data stringa JSON.
    """

    info = jsonpickle.decode(DataJson)

    ingredients_to_remove = info['ingredients_to_remove']
    ingredients_to_add = info['ingredients_to_add']
    
    return ingredients_to_remove, ingredients_to_add


def calculate_nutritional_facts_of_recipe(ingredients_names, quantites):
    """
    Calcola i valori nutrizionali totali di una ricetta, dati in input i nomi degli ingredienti usati nella ricetta
    con le rispettive quantitità.
    
    Args : 
    - ingredients_names : lista di stringhe, rappresentanti i nomi degli ingredienti presenti nella ricetta
    - quantites : quantità corrispondenti degli ingredienti presenti nella ricetta
    
    Returns :
    - nutritional_facts : alori nutrizionali totali della ricetta.
    """

    # inizializzazione valori nutrizionali ricetta
    nutritional_facts = {
        'servingSize [g]':0,
        'calories [cal]': 0,
        'totalFat [g]': 0,
        'saturatedFat [g]': 0,
        'totalCarbohydrate [g]': 0,
        'protein [g]': 0,
        'sugars [g]': 0,
        'dietaryFiber [g]': 0,
        'cholesterol [mg]': 0,
        'sodium [mg]': 0
    }

    # per ogni ingrediente aggiungiamo la quantità in relazione a suoi valori per 100g
    for ingredient, quantity in zip(ingredients_names, quantites):
        nut_facts_of_ing = ingredientService.get_nutritional_facts(ingredient.name)
        nutritional_facts['servingSize [g]'] += int(quantity)
        if nut_facts_of_ing != None:
            for nut_fact in nutritional_facts:
                val = nut_facts_of_ing.get(nut_fact, 0) or 0  
                nutritional_facts[nut_fact] += val * (int(quantity)/100)

    return nutritional_facts



def _normalize(score, best_value):
    """
    Effettua la normalizzazione di uno score rispetto a un valore di riferimento massimo.

    Args : 
    - score : punteggio da normalizzare.
    - best_value : miglior valore possibile, di riferimento massimo.

    Returns :
    - score_normalizzato : punteggio normalizzato.
    """
    if best_value == 0:
        return 0
    else:
        return score / best_value



def _score_who_value(value, lower_bound, upper_bound, minimize=True, normalize=False):
    """
    Calculates a score for a single value. The resulting score is between [0,1] while 0 is the worst possible score, and
     1 the best.
    
    Args :
    - value: The to-be-scored nutrient value.
    - lower_bound: The lower bound (based on the 100g normalization).
    - upper_bound: The upper bound (based on the 100g normalization).
    - minimize: Optional parameter which inverts the result when the nutrient value shall be maximized instead.
    - normalize: If the result shall be normalized to [0,1]. Does only work for results which are numbers.
    
    Returns:
    - score :  a score is 0, 1, or 2 (between [0,1] when normalized) while 0 is the worst possible score, and 1 the best.
    """

    if normalize:
        if value < lower_bound:  # score is very good (low/green category)
            score = 1
        elif value > upper_bound:  # score is very bad (high/red category)
            score = 0
        else:  # scores in the medium/amber category
            score = 1 - (value - lower_bound) / (upper_bound - lower_bound)

        if minimize:
            return score
        else:  # a score which maximizes the value (thus a high value instead a low one is good) is inverted
            return 1 - score
    else:
        if minimize:
            if value < lower_bound:
                return 2
            elif value < upper_bound:
                return 1
            else:
                return 0
        else:
            if value < lower_bound:
                return 0
            elif value < upper_bound:
                return 1
            else:
                return 2

def compute_who_score_of_custom_recipe(protein, total_carbohydrate, sugars, total_fat, saturated_fat, dietary_fiber, sodium, serving_size,
              normalization_comment, normalize=False):
    """
    Calculates the WHO-Score. The range is 0-14, with 14 as the best.

    Args : 
    - protein: The proteins in g per 100 g.
    - total_carbohydrate: The carbohydrates in g per 100 g.
    - sugars: The sugar in g per 100 g.
    - total_fat: The fat in g per 100 g.
    - saturated_fat: The saturated fat in g per 100 g.
    - dietary_fiber: The dietary fiber in g per 100 g.
    - sodium: The sodium in g per 100 g.
    - serving_size: The size of a single portion.
    - normalization_comment: The comment from the normalization.
    - normalize: Whether the result shall be normalized in the range [0,1] or not. Default is False.
    
    Returs:
    - who_score : The WHO-Score
    """

    # WHO score requires the daylie sodium value. As there are no user information here, we take the next best value-
    # the sodium amount per portion (assuming the user eats one portion)
    # Also, re-factor the normalization process.
    if normalization_comment == '' and serving_size > 0:
        sodium_per_serving = sodium / 100 * serving_size
    else:  # for recipes with problematic normalization return an invalid score
        sodium_per_serving = float('nan')

    score = sum([_score_who_value(protein, lower_bound=10, upper_bound=15, normalize=normalize, minimize=False),
                 _score_who_value(total_carbohydrate, lower_bound=55, upper_bound=75, normalize=normalize,
                                  minimize=False),
                 _score_who_value(sugars, lower_bound=0, upper_bound=10, normalize=normalize),
                 _score_who_value(total_fat, lower_bound=15, upper_bound=30, normalize=normalize),
                 _score_who_value(saturated_fat, lower_bound=0, upper_bound=10, normalize=normalize),
                 _score_who_value(dietary_fiber, lower_bound=0, upper_bound=3, normalize=normalize, minimize=False),
                 _score_who_value(sodium_per_serving, lower_bound=0, upper_bound=2)])

    if normalize:
        return _normalize(score, 14)
    else:
        return score



