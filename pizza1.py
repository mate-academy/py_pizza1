"""Make pizza module"""


class Pizza:
    """Standart pizza class"""
    def __init__(self):
        self._ingredients = ["ham", "tomatoes", "cheese"]

    def show_ingredients(self):
        """
        :return: list with ingredients
        """
        return self._ingredients

    def make_recipe(self):
        """
        :return: pizza recipe
        """
        result = "Make dough\n"
        for i in self._ingredients:
            result += f"Add {i}\n"
        result += "Bake"
        return result


class PopcornPizza(Pizza):
    """Popcorn pizza class"""
    def __init__(self):
        super().__init__()
        self._ingredients = ["ham", "popcorn", "cheese"]


class ChoclatePizza(Pizza):
    """Choclate pizza class"""
    def __init__(self):
        super().__init__()
        self._ingredients = ["fish", "popcorn", "chocolate"]
