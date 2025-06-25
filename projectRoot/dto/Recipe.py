import jsonpickle
from typing import Optional, Dict
from .Schema import HealthinessInfo, SustainabilityInfo

class Recipe:

    def __init__(self, name, explanation, ingredients, healthiness: Optional[HealthinessInfo], sustainability: Optional[SustainabilityInfo], nutritional_values: Dict[str, float]):
        self.name = name
        self.explanation = explanation
        self.ingredients = ingredients
        self.healthiness = healthiness
        self.sustainability = sustainability
        self.nutritional_values = nutritional_values


    def to_json(self):
        return jsonpickle.encode(self)

    def from_json(self, json_string):
        obj = jsonpickle.decode(json_string)
        return self.from_dict(obj.__dict__)

    def from_dict(self, data):
        name = data.get("name", "")
        explanation = data.get("explanation", "")

        ingr_data = data.get("ingredients", {})
        if isinstance(ingr_data, list):
            ingredients = ingr_data
        elif isinstance(ingr_data, dict):
            names = ingr_data.get("ingredients", [])
            quants = ingr_data.get("quantities", [])
            ingredients = list(zip(names, quants))
        else:
            ingredients = []

        healthiness_score = data.get("healthiness_score", "")
        sustainability_score = data.get("sustainability_score", "")
        nutr = data.get("nutritional_values", {})
        nutritional_values = {k: float(v) for k, v in nutr.items()}

        return Recipe(name, explanation, ingredients, healthiness_score, sustainability_score, nutritional_values)

    def from_recommendation_dict(self, rec_item):
        food_info = rec_item.get("food_info", {})

        self.name = food_info.get("food_item", "")
        self.explanation = rec_item.get("explanation", "")

        ingr_data = food_info.get("ingredients", {})
        names = ingr_data.get("ingredients", [])
        quants = ingr_data.get("quantities", [])
        self.ingredients = list(zip(names, quants))

        healthiness_data = food_info.get("healthiness", {})
        sustainability_data = food_info.get("sustainability", {})
        self.healthiness = HealthinessInfo(**healthiness_data) if healthiness_data else None
        self.sustainability = SustainabilityInfo(**sustainability_data) if sustainability_data else None

        nutr = food_info.get("nutritional_values", {})
        self.nutritional_values = {k: float(v) for k, v in nutr.items()}

        

    def from_alternative_dict(self, alt_item):
        self.name = alt_item.get("food_item", "")
        self.explanation = ""

        # Ingredienti
        ingr_data = alt_item.get("ingredients")
        if ingr_data is None:
          self.ingredients = []
        else:
          names = ingr_data.get("ingredients", [])
          quants = ingr_data.get("quantities", [])
          self.ingredients = list(zip(names, quants))

        healthiness_data = alt_item.get("healthiness", {})
        sustainability_data = alt_item.get("sustainability", {})
        self.healthiness = HealthinessInfo(**healthiness_data) if healthiness_data else None
        self.sustainability = SustainabilityInfo(**sustainability_data) if sustainability_data else None

        nutr = alt_item.get("nutritional_values", {})
        self.nutritional_values = {k: float(v) for k, v in nutr.items()}

        


    def from_foodinfo_dict(self, food_info):
        self.name = food_info.get("food_item", "")
        self.explanation = ""  # food_info non ha explanation

        ingr_data = food_info.get("ingredients", {})
        names = ingr_data.get("ingredients", [])
        quants = ingr_data.get("quantities", [])
        self.ingredients = list(zip(names, quants))

        healthiness_data = food_info.get("healthiness", {})
        sustainability_data = food_info.get("sustainability", {})
        self.healthiness = HealthinessInfo(**healthiness_data) if healthiness_data else None
        self.sustainability = SustainabilityInfo(**sustainability_data) if sustainability_data else None

        nutr = food_info.get("nutritional_values", {})
        self.nutritional_values = {k: float(v) for k, v in nutr.items()}

        

    def display(self):
        print("\n" + "-"*90)
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

        print("-"*90)
