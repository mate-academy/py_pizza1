import pizza1


def test_pizza():
    p = pizza1.Pizza()
    assert p.make_recipe() == """Make dough
Add ham
Add tomatoes
Add cheese
Bake"""


def test_add_new_ingr_pizza():
    p = pizza1.Pizza()
    p.add_ingredient('strawberry')
    assert p.make_recipe() == """Make dough
Add ham
Add tomatoes
Add cheese
Add strawberry
Bake"""


def test_replace_ingr_pizza():
    p = pizza1.Pizza()
    p.replace_ingredient('tomatoes', 'cherry')
    assert p.make_recipe() == """Make dough
Add ham
Add cherry
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
    p = pizza1.ChocolatePizza()
    assert p.make_recipe() == """Make dough
Add fish
Add popcorn
Add chocolate
Bake"""
