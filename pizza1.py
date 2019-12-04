"""Create a class to generate pizza recipe."""


class Pizza:
    """pizza representation"""
    def make_recipe(self):
        """make pizza"""
        return ("Make dough\n" +
                self.set_first_ing() + "\n" +
                self.set_second_ing() + "\n" +
                self.set_third_ing() + "\n" +
                "Bake")

    @staticmethod
    def set_first_ing():
        """get first ing"""
        return "Add ham"

    @staticmethod
    def set_second_ing():
        """get second ing"""
        return "Add tomatoes"

    @staticmethod
    def set_third_ing():
        """get third ing"""
        return "Add cheese"


class PopcornPizza(Pizza):
    """delicious pizza """
    def set_first_ing(self):
        """return first ing"""
        return "Add ham"

    def set_second_ing(self):
        """return second ing"""
        return "Add popcorn"

    def set_third_ing(self):
        """return third ing"""
        return "Add cheese"


class ChoclatePizza(Pizza):
    """delicious pizza """
    def set_first_ing(self):
        """return first ing"""
        return "Add fish"

    def set_second_ing(self):
        """return second ing"""
        return "Add popcorn"

    def set_third_ing(self):
        """return third ing"""
        return "Add chocolate"
