"""
docstring
"""


class Pizza:
    """
    pizza recipe
    """

    def make_recipe(self):
        """

        :return:
        """
        return ("Make dough\n" +
                self.ing_one() + "\n" +
                self.ing_two() + "\n" +
                self.ing_three() + "\n" +
                "Bake")

    @staticmethod
    def ing_one():
        """

        :return:
        """
        return "Add ham"

    @staticmethod
    def ing_two():
        """

        :return:
        """
        return "Add tomatoes"

    @staticmethod
    def ing_three():
        """

        :return:
        """
        return "Add cheese"


class PopcornPizza(Pizza):
    """
    popcornpizze recipe
    """

    def ing_one(self):
        """

        :return:
        """
        return "Add ham"

    def ing_two(self):
        """

        :return:
        """
        return "Add popcorn"

    def ing_three(self):
        """

        :return:
        """
        return "Add cheese"


class ChoclatePizza(Pizza):
    """
    choclatepizze recipe
    """

    def ing_one(self):
        """

        :return:
        """
        return "Add fish"

    def ing_two(self):
        """

        :return:
        """
        return "Add popcorn"

    def ing_three(self):
        """

        :return:
        """
        return "Add chocolate"
