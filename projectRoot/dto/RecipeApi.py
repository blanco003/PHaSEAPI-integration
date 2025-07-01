import json
from typing import Optional, Dict
from .SchemaApi import HealthinessInfo, SustainabilityInfo


class RecipeApi:
    def __init__(self, name: str, explanation: str, ingredients: list, healthiness: Optional[HealthinessInfo], sustainability: Optional[SustainabilityInfo], nutritional_values: Optional[dict[str, Optional[float]]], food_item_url: Optional[str]):
        self.name = name
        self.explanation = explanation
        self.ingredients = ingredients
        self.healthiness = healthiness
        self.sustainability = sustainability
        self.nutritional_values = nutritional_values
        self.food_item_url = food_item_url

    def to_dict(self):
        return {
            "name": self.name,
            "explanation": self.explanation,
            "ingredients": self.ingredients,
            "healthiness": self.healthiness.to_dict() if self.healthiness else None,
            "sustainability": self.sustainability.to_dict() if self.sustainability else None,
            "nutritional_values": self.nutritional_values,
            "food_item_url": self.food_item_url
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_string):
        data = json.loads(json_string)
        return Recipe.from_dict(data)

    @staticmethod
    def from_dict(data):
        name = data.get("name", "")
        explanation = data.get("explanation", "")

        # Fix parsing ingredients
        ingr_data = data.get("ingredients", [])
        ingredients = []
        for i in ingr_data:
            if isinstance(i, dict) and "py/tuple" in i:
                ingredients.append(tuple(i["py/tuple"]))
            elif isinstance(i, list) and len(i) == 2:
                ingredients.append(tuple(i))
            else:
                # fallback in caso di errore strutturale
                ingredients.append((str(i), ""))

        # Healthiness & Sustainability
        h_data = data.get("healthiness")
        s_data = data.get("sustainability")
        healthiness = HealthinessInfo.from_dict(h_data) if h_data else None
        sustainability = SustainabilityInfo.from_dict(s_data) if s_data else None

        nutr = data.get("nutritional_values", {})
        nutritional_values = {k: float(v) for k, v in nutr.items()}

        food_item_url = data.get("food_item_url", "")

        return Recipe(name, explanation, ingredients, healthiness, sustainability, nutritional_values, food_item_url)



    def from_recommendation_dict(self, rec_item):
        food_info = rec_item.get("food_info", {})

        self.name = food_info.get("food_item", "")
        self.explanation = rec_item.get("explanation", "")
        
        ingr_data = food_info.get("ingredients", {})
        names = ingr_data.get("ingredients", [])
        quants = ingr_data.get("quantities", [])
        self.ingredients = list(zip(names, quants))

        h_data = food_info.get("healthiness", {})
        s_data = food_info.get("sustainability", {})
        self.healthiness = HealthinessInfo.from_dict(h_data) if h_data else None
        self.sustainability = SustainabilityInfo.from_dict(s_data) if s_data else None

        nutr = food_info.get("nutritional_values", {})
        self.nutritional_values = {k: float(v) for k, v in nutr.items()}

        self.food_item_url = food_info.get("food_item_url", "")

    def from_alternative_dict(self, alt_item):
        self.name = alt_item.get("food_item", "")
        self.explanation = ""

        ingr_data = alt_item.get("ingredients")
        if ingr_data is None:
            self.ingredients = []
        else:
            names = ingr_data.get("ingredients", [])
            quants = ingr_data.get("quantities", [])
            self.ingredients = list(zip(names, quants))

        h_data = alt_item.get("healthiness", {})
        s_data = alt_item.get("sustainability", {})
        self.healthiness = HealthinessInfo.from_dict(h_data) if h_data else None
        self.sustainability = SustainabilityInfo.from_dict(s_data) if s_data else None

        nutr = alt_item.get("nutritional_values", {})
        self.nutritional_values = {
            k: float(v) for k, v in nutr.items() if v is not None
        }   

        self.food_item_url = alt_item.get("food_item_url", "")


    def from_foodinfo_dict(self, food_info):
        self.name = food_info.get("food_item", "")
        self.explanation = ""

        ingr_data = food_info.get("ingredients", {})
        names = ingr_data.get("ingredients", [])
        quants = ingr_data.get("quantities", [])
        self.ingredients = list(zip(names, quants))

        h_data = food_info.get("healthiness", {})
        s_data = food_info.get("sustainability", {})
        self.healthiness = HealthinessInfo.from_dict(h_data) if h_data else None
        self.sustainability = SustainabilityInfo.from_dict(s_data) if s_data else None

        nutr = food_info.get("nutritional_values", {})
        self.nutritional_values = {
            k: float(v) for k, v in nutr.items() if v is not None
        }   

        self.food_item_url = food_info.get("food_item_url", "")

    def display(self):
        print("\n" + "-" * 90)
        print(f"\nName : {self.name}")
        print(f"Spiegazione: {self.explanation}")

        print(f"\nHealthiness Score: {self.healthiness.score if self.healthiness else 'N/A'}")
        if self.healthiness and self.healthiness.qualitative:
            print(f"  • Qualitative: {self.healthiness.qualitative}")

        print(f"\nSustainability Score: {self.sustainability.score if self.sustainability else 'N/A'}")
        if self.sustainability:
            if self.sustainability.qualitative:
                print(f"  • Qualitative: {self.sustainability.qualitative}")
            if self.sustainability.CF is not None:
                print(f"  • CF: {self.sustainability.CF}")
            if self.sustainability.WF is not None:
                print(f"  • WF: {self.sustainability.WF}")

        if self.ingredients:
            print("\nIngredienti:")
            for ingrediente, quantita in self.ingredients:
                print(f"  - {ingrediente}: {quantita}")
        else:
            print("\nIngredienti: N/A")

        print("\nValori nutrizionali:")
        for nutriente, valore in self.nutritional_values.items():
            print(f"  • {nutriente}: {valore}")

        print(f"\nURL : {self.food_item_url}")

        print("-" * 90)
