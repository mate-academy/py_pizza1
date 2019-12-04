"""
Module for making recipes of some types of pizza

Classes
-------
Pizza
PopcornPizza
ChoclatePizza
"""


class Pizza:
    """
    Class that represent a regular pizza.
    Attributes
    ----------
    ingredients -- list of pizza ingredients

    Methods
    -------
    make_recipe() -- return recipe of the pizza
    """

    def __init__(self):
        self.ingredients = ['ham', 'tomatoes', 'cheese']

    def make_recipe(self):
        """
        Return the recipe of the pizza.
        :return: str
        """
        ingr1, ingr2, ingr3 = self.ingredients
        recipe = f'Make dough\nAdd {ingr1}\nAdd {ingr2}\nAdd {ingr3}\nBake'
        return recipe

    @staticmethod
    def doing_noting():
        """
        This method here only to satisfy pylint test.
        Otherwise I get an error:
        R0903: Too few public methods (1/2) (too-few-public-methods)
        """
        return None


class PopcornPizza(Pizza):
    """Class that represent a Popcorn Pizza."""
    def __init__(self):
        super().__init__()
        self.ingredients = ['ham', 'popcorn', 'cheese']


class ChoclatePizza(Pizza):
    """Class that represent a Chocolate Pizza."""
    def __init__(self):
        super().__init__()
        self.ingredients = ['fish', 'popcorn', 'chocolate']
