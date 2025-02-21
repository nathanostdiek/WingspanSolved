# src/entities/bird.py

class Bird:
    def __init__(self, common_name, scientific_name, set_name, color, power_text, flavor_text, victory_points, nest_type, egg_limit, wingspan, habitats, food_cost, interchangeable_food_cost, total_food_cost, bonus_categories):
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.set_name = set_name
        self.color = color
        self.power_text = power_text
        self.flavor_text = flavor_text
        self.victory_points = victory_points
        self.nest_type = nest_type
        self.egg_limit = egg_limit
        self.wingspan = wingspan
        self.habitats = habitats
        self.food_cost = food_cost
        self.interchangeable_food_cost = interchangeable_food_cost
        self.total_food_cost = total_food_cost
        self.bonus_categories = bonus_categories

    def __repr__(self):
        return (f"Bird(common_name={self.common_name}, scientific_name={self.scientific_name}, "
                f"set_name={self.set_name}, color={self.color}, victory_points={self.victory_points}, habitats={self.habitats}, food_cost={self.food_cost}, interchangeable_food_cost={self.interchangeable_food_cost}, total_food_cost={self.total_food_cost}, bonus_categories={self.bonus_categories})")