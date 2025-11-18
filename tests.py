from decimal import Decimal
from fixtures import cart, laptop, mouse
# from fixtures import event_bus
from main import Item, Cart


def test_item_creation(laptop):
    """Verifica creación basica de Item"""
    assert laptop.id == "item-001"
    assert laptop.name == "Laptop"
    assert laptop.price == Decimal("999.99")
    assert laptop.quantity == 1


def test_cart_add_item(cart, laptop):
    """Verifica añadir item al carrito"""
    cart.add_item(laptop)
    
    items = cart.get_items()
    assert len(items) == 1
    assert items[0].id == "item-001"


def test_cart_total_calculation(cart, laptop, mouse):
    """Verifica calculo del total"""
    cart.add_item(laptop)
    cart.add_item(mouse)
    
    expected_total = Decimal("999.99") + Decimal("29.99")
    assert cart.get_total() == expected_total


def test_cart_duplicate_item_increments_quantity(cart, laptop):
    """Verifica que añadir item duplicado incrementa cantidad"""
    cart.add_item(laptop)
    cart.add_item(Item(id="item-001", name="Laptop", price=Decimal("999.99"), quantity=1))
    
    items = cart.get_items()
    assert len(items) == 1
    assert items[0].quantity == 2


def test_end_to_end():
    pass  # Test con lo que un usuario deberia hacer para usar el software