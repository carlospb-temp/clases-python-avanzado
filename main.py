from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class EventBus:
    a: int
    
    def subscribe(self):
        pass


@dataclass
class Item:
    id: str
    name: str
    price: Decimal
    quantity: int


@dataclass
class Cart:
    cart_id: str
    event_bus: EventBus = field(default_factory=EventBus())
    _items: dict = field(default_factory=dict)
    
    def add_item(self, item) -> Item:
        """Adds item to the cart. Returns item added."""
        if item.id in self._items.keys():
            self._items[item.id].quantity += 1
        else:
            self._items[item.id] = item
        return self._items[item.id]

    def get_items(self) -> list[Item]:
        """Returns a list of the items in the cart."""
        return self._items.values()
    
    def get_total(self) -> Decimal:
        """Returns the total price of the cart."""
        return sum([item.price * item.quantity for item in self._items.values()])


if __name__ == "__main__":
    event_bus = EventBus(0)
    cart = Cart(cart_id="cart_01", event_bus=event_bus)