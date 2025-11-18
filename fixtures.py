import pytest
from main import Item, Cart
from decimal import Decimal


@pytest.fixture
def cart():
    """Carrito conectado al EventBus"""
    return Cart(cart_id="cart-001")

@pytest.fixture
def laptop():
    """Item de ejemplo: Laptop"""
    return Item(
        id="item-001",
        name="Laptop",
        price=Decimal("999.99"),
        quantity=1
    )

@pytest.fixture
def mouse():
    """Item de ejemplo: Mouse"""
    return Item(
        id="item-002",
        name="Mouse",
        price=Decimal("29.99"),
        quantity=1
    )