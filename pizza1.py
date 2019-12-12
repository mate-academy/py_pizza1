"""
Pizza
PopcornPizza
ChocolatePizza
"""


class Pizza:
    """
    pizza
    """
    def __init__(self):
        super().__init__()
        self._ingridients = [
            'ham',
            'tomatoes',
            'cheese',
        ]

    def add_ingredient(self, value):
        """
        add_ingredient
        """
        self._ingridients.append(value)

    def make_recipe(self):
        """
        make_reciepe
        """
        pizza = "Make dough\nAdd """
        pizza += "\nAdd ".join(self._ingridients)
        pizza += "\nBake"
        return pizza


class PopcornPizza(Pizza):
    """
    popcornPizza
    """
    def __init__(self):
        super().__init__()
        self._ingridients = [
            'ham',
            'popcorn',
            'cheese',
        ]


class ChoclatePizza(Pizza):
    """
    chocolatePizza
    """
    def __init__(self):
        super().__init__()
        self._ingridients = [
            'fish',
            'popcorn',
            'chocolate',
        ]
