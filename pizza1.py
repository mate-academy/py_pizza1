"""Create a class to generate pizza recipe.
Provide the ability to change ingredients in subclasses."""


class Pizza:
    """Pizza representation"""

    def __init__(self):
        self.recipe = 'Make dough'
        self.ingredient_one = 'Add ham'
        self.ingredient_two = 'Add tomatoes'
        self.ingredient_three = 'Add cheese'
        self.bake = 'Bake'

    def make_recipe(self):
        """Make recipe with iterating over an instance object's"""
        return '\n'.join([v for k, v in self.__dict__.items()])

    def __str__(self):
        return self.__class__.__name__


class PopcornPizza(Pizza):
    """Popcorn pizza representation"""
    def __init__(self):
        super().__init__()
        self.ingredient_one = 'Add ham'
        self.ingredient_two = 'Add popcorn'
        self.ingredient_three = 'Add cheese'

    def __str__(self):
        return self.__class__.__name__


class ChocolatePizza(Pizza):
    """Chocolate pizza representation"""
    def __init__(self):
        super().__init__()
        self.ingredient_one = 'Add fish'
        self.ingredient_two = 'Add popcorn'
        self.ingredient_three = 'Add chocolate'

    def __str__(self):
        return self.__class__.__name__
