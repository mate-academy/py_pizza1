"""Make pizza module"""


class Pizza:
    """Standart pizza class"""
    def __init__(self):
        self._ingredients = ["ham", "tomatoes", "cheese"]

    def make_recipe(self):
        """
        :return: pizza recipe
        """
        recipe = GeneratePizzaRecipe(self._ingredients)
        return recipe.make_recipe()

    def add_ingredient(self, ingredient):
        """
        :param ingredient: add argument to ingredients
        :return: None
        """
        self._ingredients.append(ingredient)



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

class GeneratePizzaRecipe:
    """Class for generate pizza recipe"""
    def __init__(self, ingredients):
        self._ingredients = ingredients

    def __str__(self):
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
