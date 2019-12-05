class Pizza:
    def get_recipe(self):
        return "Make dough\n" + \
               self.get_ing1() + "\n" + \
               self.get_ing2() + "\n" + \
               self.get_ing3() + "\n" + \
               + "Bake"

    def get_ing1(self):
        return "Add ham"

    def get_ing2(self):
        return "Add tomatoes"

    def get_ing3(self):
        return "Add cheese"


class ChocolatePizza(Pizza):
    def get_ing1(self):
        return "Add fish"

    def get_ing2(self):
        return "Add popcorn"

    def get_ing3(self):
        return "Add chocolate"
