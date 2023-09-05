import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    lasanha_presunto = Dish("lasanha presunto", 25.90)
    mais_lasanha_presunto = Dish("lasanha presunto", 25.90)
    lasanha_berinjela = Dish("lasanha berinjela", 27.00)

    assert lasanha_presunto.name == "lasanha presunto"
    assert lasanha_presunto.price == 25.90

    assert lasanha_presunto == mais_lasanha_presunto
    assert lasanha_presunto != lasanha_berinjela

    assert hash(lasanha_presunto) == hash(mais_lasanha_presunto)
    assert hash(lasanha_presunto) != hash(lasanha_berinjela)
    assert repr(lasanha_presunto) == "Dish('lasanha presunto', R$25.90)"

    with pytest.raises(TypeError):
        Dish("lasanha berinjela", "27.00")
    with pytest.raises(ValueError):
        Dish("lasanha berinjela", -27.00)

    mussarela = Ingredient("queijo mussarela")

    lasanha_presunto.add_ingredient_dependency(mussarela, 15)
    assert lasanha_presunto.recipe.get(mussarela) == 15
    assert lasanha_presunto.get_restrictions() == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert lasanha_presunto.get_ingredients() == {
        mussarela
    }
