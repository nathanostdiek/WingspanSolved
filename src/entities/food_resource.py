# src/entities/food_resource.py
from enum import Enum

class FoodResourceType(Enum):
    NECTAR = "Nectar"
    FRUIT = "Fruit"
    FISH = "Fish"
    INVERTEBRATE = "Invertebrate"
    RODENT = "Rodent"
    SEED = "Seed"
    # the pinwheel of any food (NOT NECTAR)
    WILD = "Wild (food)"

class FoodResource:
    def __init__(self, type: FoodResourceType):
        if not isinstance(type, FoodResourceType):
            raise ValueError(f"Invalid food resource type: {type}")
        self.type = type

    def __repr__(self):
        return f"FoodResource(type={self.type})"