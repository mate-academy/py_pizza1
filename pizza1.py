"""modules"""


class Pizza:
    """class to represent usual pizza"""

    def make_recipe(self):
        """return recipe for pizza"""
        return ("Make dough\n" +
                self.get_first_ingredient() + "\n" +
                self.get_second_ingredient() + "\n" +
                self.get_third_ingredient() + "\n" +
                "Bake")

    @staticmethod
    def get_first_ingredient():
        """return list of ingredients"""
        return "Add ham"

    @staticmethod
    def get_second_ingredient():
        """return list of ingredients"""
        return "Add tomatoes"

    @staticmethod
    def get_third_ingredient():
        """return list of ingredients"""
        return "Add cheese"


class PopcornPizza(Pizza):
    """class to represent special kind of pizza with popcorn"""

    def get_first_ingredient(self):
        """return list of ingredients"""
        return "Add ham"

    def get_second_ingredient(self):
        """return list of ingredients"""
        return "Add popcorn"

    def get_third_ingredient(self):
        """return list of ingredients"""
        return "Add cheese"


class ChocolatePizza(Pizza):
    """class to represent special kind of pizza with chocolate"""

    def get_first_ingredient(self):
        """return list of ingredients"""
        return "Add fish"

    def get_second_ingredient(self):
        """return list of ingredients"""
        return "Add popcorn"

    def get_third_ingredient(self):
        """return list of ingredients"""
        return "Add chocolate"
