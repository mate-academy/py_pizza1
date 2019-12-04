"""modules"""


class Pizza:
    """class to represent usual pizza"""
    def __init__(self):
        self.ingredients = ["ham", "tomatoes", "cheese"]

    def make_recipe(self):
        """return recipe for pizza"""
        recipe = "Make dough\n"
        for ingredient in self.ingredients:
            recipe += f"Add {ingredient}\n"
        return recipe + "Bake"

    def get_ingredients(self):
        """return list of ingredients"""
        return self.ingredients


class PopcornPizza(Pizza):
    """class to represent special kind of pizza with popcorn"""
    def __init__(self):
        super().__init__()
        self.ingredients = ["ham", "popcorn", "cheese"]


class ChocolatePizza(Pizza):
    """class to represent special kind of pizza with chocolate"""
    def __init__(self):
        super().__init__()
        self.ingredients = ["fish", "popcorn", "chocolate"]
