"""
module for making delicious pizza
"""


class Pizza:
    """
    Class that creates delicious pizza.
    """

    def __init__(self):
        self.ingrts = ['ham', 'tomatoes', 'cheese']

    def add_ingredient(self, ingrt):
        """
        Add ingredient in recipe for making pizza.
        :param ingrt:
        :return:
        """
        return self.ingrts.append(ingrt)

    def replace_ingredient(self, prev_ingrt, new_ingrt):
        """
        Replace ingredient in recipe for making pizza.
        :param prev_ingrt:
        :param new_ingrt:
        :return:
        """
        return [new_ingrt if ingrt == prev_ingrt else ingrt for ingrt in self.ingrts]

    def make_recipe(self):
        """
        Return recipe for making pizza.
        :return: str
        """
        add_ingrts = ['Add ' + ingrt for ingrt in self.ingrts]
        return 'Make dough\n' + '\n'.join(add_ingrts) + '\nBake'


class PopcornPizza(Pizza):
    """
    Class that creates delicious popcorn pizza.
    """

    def __init__(self):
        super().__init__()
        self.ingrts = ['ham', 'popcorn', 'cheese']


class ChocolatePizza(Pizza):
    """
        Class that creates chocolate pizza.
    """

    def __init__(self):
        super().__init__()
        self.ingrts = ['fish', 'popcorn', 'chocolate']
