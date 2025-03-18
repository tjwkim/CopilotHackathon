from typing import List
from src.product import Product

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def remove_product(self, product_id: int):
        self.items = [item for item in self.items if item.id != product_id]

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)