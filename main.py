from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Item:
    """Represents an item.
    
    Attributes:
        id (str)
        name (str)
        price (decimal)
        quantity (int)
    """
    id: str
    name: str
    price: Decimal
    quantity: int


@dataclass
class Cart:
    """Represents a shopping cart.
    
    Attributes:
        cart_id (str)
    """
    cart_id: str
    _items: dict = field(default_factory=dict)

    def add_item(self, item) -> Item:
        """Adds item to the cart. Returns item added.

        Args:
            item (Item): the item to be added.

        Returns:
            Item: the item added.
        """
        if item.id in self._items.keys():
            self._items[item.id].quantity += 1
        else:
            self._items[item.id] = item
        return self._items[item.id]

    def get_items(self) -> list[Item]:
        """Get the list of the items in the cart.

        Returns:
            list[Item]: the list of the items in the cart
        """
        return list(self._items.values())

    def get_total(self) -> Decimal:
        """Returns the total price of the cart."""
        return sum([item.price * item.quantity for item in self._items.values()])
