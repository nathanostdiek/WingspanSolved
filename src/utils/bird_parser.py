import json
from src.entities.bird import Bird
from src.entities.food_resource import FoodResourceType

def load_bonus_card_names(file_path):
    with open(file_path, 'r') as file:
        bonus_data = json.load(file)
    return [bonus["Bonus card"] for bonus in bonus_data]

def parse_bird_data(json_data, bonus_card_names):
    birds = []
    for bird_data in json_data:
        habitats = []
        # parse out habitats into list
        if bird_data.get("Forest") == "X":
            habitats.append("Forest")
        if bird_data.get("Grassland") == "X":
            habitats.append("Grassland")
        if bird_data.get("Wetland") == "X":
            habitats.append("Wetland")

        # parse food cost into list of FoodResourceType
        food_cost = []
        if bird_data.get("Seed"):
            food_cost.extend([FoodResourceType.SEED] * int(bird_data["Seed"]))
        if bird_data.get("Fish"):
            food_cost.extend([FoodResourceType.FISH] * int(bird_data["Fish"]))
        if bird_data.get("Invertebrate"):
            food_cost.extend([FoodResourceType.INVERTEBRATE] * int(bird_data["Invertebrate"]))
        if bird_data.get("Fruit"):
            food_cost.extend([FoodResourceType.FRUIT] * int(bird_data["Fruit"]))
        if bird_data.get("Rodent"):
            food_cost.extend([FoodResourceType.RODENT] * int(bird_data["Rodent"]))
        if bird_data.get("Nectar"):
            food_cost.extend([FoodResourceType.NECTAR] * int(bird_data["Nectar"]))
        if bird_data.get("Wild (food)"):
            food_cost.extend([FoodResourceType.WILD] * int(bird_data["Wild (food)"]))

        wingspan = 0
        if bird_data.get("Wingspan") == "*":
            # using -1 for * wingspans (adding bonus card logic will be complicated with this haha)
            wingspan = -1
        else:
            wingspan = int(bird_data.get("Wingspan", 0))

        # Determine if interchangeable food cost is present
        interchangeable_food_cost = "/ (food cost)" in bird_data

        # Create a list of bonus categories with "X"
        bonus_categories = [key for key in bonus_card_names if bird_data.get(key) == "X"]

        bird = Bird(
            common_name=bird_data.get("Common name", "Unknown"),
            scientific_name=bird_data.get("Scientific name", "Unknown"),
            set_name=bird_data.get("Set", "Unknown"),
            color=bird_data.get("Color", "No Power"),
            power_text=bird_data.get("Power text", ""),
            flavor_text=bird_data.get("Flavor text", ""),
            victory_points=int(bird_data.get("Victory points", 0)),
            nest_type=bird_data.get("Nest type", "Unknown"),
            egg_limit=int(bird_data.get("Egg limit", 0)),
            wingspan=wingspan,
            habitats=habitats,
            food_cost=food_cost,
            interchangeable_food_cost=interchangeable_food_cost,
            total_food_cost=int(bird_data.get("Total food cost", 0)),
            bonus_categories=bonus_categories
        )
        birds.append(bird)
    return birds

def load_bird_data(bird_file_path, bonus_file_path):
    bonus_card_names = load_bonus_card_names(bonus_file_path)
    with open(bird_file_path, 'r') as file:
        bird_data_json = json.load(file)
    return parse_bird_data(bird_data_json, bonus_card_names) 