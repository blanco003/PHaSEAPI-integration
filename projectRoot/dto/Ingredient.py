import jsonpickle
from typing import Optional, Dict
from .Schema import HealthinessInfo, SustainabilityInfo


class Ingredient:

    def __init__(self, name, food_item_type, ingredients, healthiness: Optional[HealthinessInfo], sustainability: Optional[SustainabilityInfo], nutritional_values: Dict[str, float]):
        self.name = name
        self.food_item_type = food_item_type
        self.ingredients = ingredients
        self.healthiness = healthiness
        self.sustainability = sustainability
        self.nutritional_values = nutritional_values

    def from_dict(self, data):
        name = data.get("food_item", "")
        food_item_type = data.get("food_item_type", "")

        ingr_data = data.get("ingredients")
        if ingr_data is None:
            ingredients = []
        else:
            names = ingr_data.get("ingredients", [])
            quants = ingr_data.get("quantities", [])
            ingredients = list(zip(names, quants)) if quants else [(name, "") for name in names]

        healthiness_data = data.get("healthiness", {})
        sustainability_data = data.get("sustainability", {})
        healthiness = HealthinessInfo(**healthiness_data) if healthiness_data else None
        sustainability = SustainabilityInfo(**sustainability_data) if sustainability_data else None

        nutr = data.get("nutritional_values", {})
        nutritional_values = {k: float(v) for k, v in nutr.items()}

        return Ingredient(name, food_item_type, ingredients, healthiness, sustainability, nutritional_values)

    def display(self):
        print("\n" + "-" * 90)
        print(f"\nName : {self.name}")
        print(f"Tipo : {self.food_item_type}")

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

        print("-" * 90)