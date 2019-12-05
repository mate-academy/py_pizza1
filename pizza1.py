"""
Create a class to generate pizza recipe.
Provide the ability to change ingredients in subclasses.
"""


class Pizza:
    """Pizza class"""

    def make_recipe(self):
        """Returns pizza recipe"""
        return ("Make dough\n" +
                self.get_ing1() + "\n" +
                self.get_ing2() + "\n" +
                self.get_ing3() + "\n" +
                "Bake")

    @staticmethod
    def get_ing1():
        """Returns pizza ingredients"""
        return "Add ham"

    @staticmethod
    def get_ing2():
        """Returns pizza ingredients"""
        return "Add tomatoes"

    @staticmethod
    def get_ing3():
        """Returns pizza ingredients"""
        return "Add cheese"


class PopcornPizza(Pizza):
    """PopcornPizza subclass Pizza"""

    @staticmethod
    def get_ing1():
        """Returns pizza ingredients"""
        return "Add ham"

    @staticmethod
    def get_ing2():
        """Returns pizza ingredients"""
        return "Add popcorn"

    @staticmethod
    def get_ing3():
        """Returns pizza ingredients"""
        return "Add cheese"


class ChoclatePizza(Pizza):
    """ChoclatePizza subclass Pizza"""


    @staticmethod
    def get_ing1():
        """Returns pizza ingredients"""
        return "Add fish"


    @staticmethod
    def get_ing2():
        """Returns pizza ingredients"""
        return "Add popcorn"


    @staticmethod
    def get_ing3():
        """Returns pizza ingredients"""
        return "Add chocolate"
