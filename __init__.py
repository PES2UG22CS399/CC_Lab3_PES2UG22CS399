from typing import List

from products import dao


class Product:
    """Represents a product with its attributes."""

    def __init__(self, id: int, name: str, description: str, cost: float, qty: int):
        """
        Initializes a Product object.

        Args:
            id: The unique identifier of the product.
            name: The name of the product.
            description: A description of the product.
            cost: The cost of the product.
            qty: The quantity of the product in stock.
        """
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> 'Product':
        """
        Creates a Product object from a dictionary.

        Args:
            data: A dictionary containing product data.

        Returns:
            A Product object.
        """
        return Product(
            data['id'], data['name'], data['description'], data['cost'], data['qty']
        )


def list_products() -> List[Product]:
    """
    Lists all available products.

    Returns:
        A list of Product objects.
    """
    products = dao.list_products()
    return [Product.load(product) for product in products]


def get_product_details(product_ids: List[int]) -> List[Product]:
    """
    Gets details for a list of product IDs.

    Args:
        product_ids: A list of product IDs.

    Returns:
        A list of Product objects corresponding to the provided IDs.
    """
    products = dao.get_products_bulk(product_ids)
    return [Product.load(product) for product in products]