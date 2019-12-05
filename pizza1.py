"""This program depicts process of pizza recipes creation"""


class Pizza:
    """This is parent class that features unique list of ingredients
    and standardised recipe creation procedure"""
    def __init__(self):
        """Initiate the list of ingredients"""
        self.list_of_ingredients = ["ham", "tomatoes", "cheese"]

    @staticmethod
    def begin():
        """May be put into return of make_recipe function directly"""
        return "Make dough\n"

    def add_smth(self):
        """Create the product mix"""
        products_mix = ""
        for ingredient in self.list_of_ingredients:
            products_mix += "Add " + ingredient + "\n"
        return products_mix

    @staticmethod
    def finish():
        """May be put into return of make_recipe function directly"""
        return "Bake"

    def make_recipe(self):
        """Finalize the recipe into one piece of text"""
        return Pizza.begin() + self.add_smth() + Pizza.finish()


class PopcornPizza(Pizza):
    """This is subclass inheriting all methods of parent class"""
    def __init__(self):
        """Distinguish the unique ingredients list"""
        super().__init__(self)
        self.list_of_ingredients = ["ham", "popcorn", "cheese"]


class ChocolatePizza(Pizza):
    """This is subclass inheriting all methods of parent class"""
    def __init__(self):
        """Distinguish the unique ingredients list"""
        super().__init__(self)
        self.list_of_ingredients = ["fish", "popcorn", "chocolate"]
