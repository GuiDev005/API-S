from uuid import UUID
from store.schemas.product import ProductIN
import pytest


def test_schemas_valited():
    data = {'name': 'Iphone 12 Pro Max', 'quantity': 10, 'price': 5989, 'status': True}
    product = ProductIN.model_validate(data)

    assert product.name == 'Iphone 12 Pro Max'
    assert isinstance(product.id, UUID)

def test_schemas_return_raise():
    data = {'name': 'Iphone 12 Pro Max', 'quantity': 10, 'price': 5989, 'status': True}
    
    with pytest.raises(ValidationError) as err:
        product = ProductIN.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 12 Pro Max", "quantity": 10, "price": 5989},
        "url": "https://errors.pydantic.dev/2.5/v/missing",
    }
    
