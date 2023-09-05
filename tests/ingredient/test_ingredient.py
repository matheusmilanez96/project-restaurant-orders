from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    massa_de_lasanha = Ingredient("massa de lasanha")
    mais_massa_de_lasanha = Ingredient("massa de lasanha")
    presunto = Ingredient("presunto")

    assert massa_de_lasanha != presunto
    assert massa_de_lasanha == mais_massa_de_lasanha

    assert hash(massa_de_lasanha) == hash("massa de lasanha")
    assert hash(massa_de_lasanha) != hash(presunto)
    assert repr(massa_de_lasanha) != repr(presunto)
    assert repr(massa_de_lasanha) == "Ingredient('massa de lasanha')"

    assert massa_de_lasanha.name == "massa de lasanha"
    assert massa_de_lasanha.restrictions == {
        Restriction.LACTOSE, Restriction.GLUTEN}

    assert massa_de_lasanha.__eq__(presunto) is False
    assert massa_de_lasanha.__eq__(mais_massa_de_lasanha) is True
