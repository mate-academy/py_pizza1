import pizza1


def test_pizza():
    p = pizza1.Pizza()
    assert p.make_recipe() == """Make dough
Add ham
Add tomatoes
Add cheese
Bake"""

def test_popcornpizza():
    p = pizza1.PopcornPizza()
    assert p.make_recipe() == """Make dough
Add ham
Add popcorn
Add cheese
Bake"""


def test_chocolatepizza():
    p = pizza1.ChoclatePizza()
    assert p.make_recipe() == """Make dough
Add fish
Add popcorn
Add chocolate
Bake"""


def test_mushroom():
    p = pizza1.Pizza()
    p.add_ingred('Mushroom')
    assert p.make_recipe() == """Make dough
Add ham
Add tomatoes
Add cheese
Add Mushroom
Bake"""