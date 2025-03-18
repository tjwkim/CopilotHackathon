import unittest
from src.cart import Cart
from src.product import Product

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product = Product(
            id=1,
            name="Test Product",
            description="Test Description",
            image_url="http://example.com/image.png",
            price=10.0,
            manufacturer="Test Manufacturer",
            model_compatibility=["Model A"],
            part_number="TP123",
            stock=10,
            specifications={"weight": "1kg"}
        )

    def test_add_product(self):
        self.cart.add_product(self.product)
        self.assertEqual(len(self.cart.items), 1)

    def test_remove_product(self):
        self.cart.add_product(self.product)
        self.cart.remove_product(self.product.id)
        self.assertEqual(len(self.cart.items), 0)

    def test_calculate_total(self):
        self.cart.add_product(self.product)
        self.assertEqual(self.cart.calculate_total(), 10.0)

if __name__ == "__main__":
    unittest.main()