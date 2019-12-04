"""
Create a class to generate pizza recipe.
Provide the ability to change ingredients in subclasses.
"""


class Pizza:
    """Pizza class"""
    def __init__(self):
        self.ingredients = ['ham', 'tomatoes', 'cheese']

    def make_recipe(self):
        """Returns pizza recipe"""
        strg = "Make dough\n"
        for i in self.ingredients:
            strg += "Add {}\n".format(i)
        return strg + "Bake"

    def get_ingredients(self):
        """Returns pizza ingredients"""
        return self.ingredients


class PopcornPizza(Pizza):
    """PopcornPizza subclass Pizza"""
    def __init__(self):
        super().__init__()
        self.ingredients = ['ham', 'popcorn', 'cheese']



class ChoclatePizza(Pizza):
    """ChoclatePizza subclass Pizza"""
    def __init__(self):
        super().__init__()
        self.ingredients = ['fish', 'popcorn', 'chocolate']
