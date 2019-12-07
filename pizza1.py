"""Module for pizza lovers"""


class Pizza:
    """Classic pizza"""
    def __init__(self):
        self._recipe = []

    def make_dough(self):
        """Make dough"""
        self._recipe.append('Make dough')

    def bake(self):
        """Baking"""
        self._recipe.append('Bake')

    def add_1st_ingredient(self):
        """First ingredient"""
        self._recipe.append('Add ham')

    def add_2nd_ingredient(self):
        """Second ingredient"""
        self._recipe.append('Add tomatoes')

    def add_3rd_ingredient(self):
        """Third ingredient"""
        self._recipe.append('Add cheese')

    def make_recipe(self):
        """Make recipe"""
        self.make_dough()
        self.add_1st_ingredient()
        self.add_2nd_ingredient()
        self.add_3rd_ingredient()
        self.bake()
        return '\n'.join(self._recipe)


class PopcornPizza(Pizza):
    """Recipe for movie lovers"""
    def add_2nd_ingredient(self):
        """Second ingredient
        (First and third ingredients are the same as for classic pizza)
        """
        self._recipe.append('Add popcorn')


class ChoclatePizza(Pizza):
    """Recipe for real gourmet"""
    def add_1st_ingredient(self):
        """First ingredient"""
        self._recipe.append('Add fish')

    def add_2nd_ingredient(self):
        """Second ingredient"""
        self._recipe.append('Add popcorn')

    def add_3rd_ingredient(self):
        """Third ingredient"""
        self._recipe.append('Add chocolate')
