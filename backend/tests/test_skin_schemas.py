import pytest
from pydantic import ValidationError
from app.modules.skins.schemas import SkinCreate,Rarity,Wear

@pytest.mark.parametrize("value", [-0.0001, 1.0001])
def test_invalid_values(value):

    with pytest.raises(ValidationError) as exc:
        SkinCreate(
            name="Redline",
            weapon="AK-47",
            rarity=Rarity.CLASSIFIED,
            wear=Wear.FACTORY_NEW,
            min_float=value,
            max_float=0.5,
            price=12.50
        )

    assert exc.value.errors()[0]["loc"] == ("min_float",)

def test_min_float_greater_than_max_float():
    with pytest.raises(ValidationError) as exc:
        SkinCreate(
            name="Redline",
            weapon="AK-47",
            rarity=Rarity.CLASSIFIED,
            wear=Wear.FACTORY_NEW,
            min_float=0.8,
            max_float=0.2,
            price=12.50
        )

    assert exc.value.errors()[0]["loc"] == ()

@pytest.mark.parametrize("value", [0.0, 0.5, 1.0])

def test_valid_float(value):
    skin = SkinCreate(
        name="Redline",
        weapon="AK-47",
        rarity=Rarity.CLASSIFIED,
        wear=Wear.FACTORY_NEW,
        min_float=value,
        max_float=value,
        price=12.50
    )

    assert skin.min_float == value
    assert skin.max_float == value