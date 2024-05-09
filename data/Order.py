import uuid
from data.User import User
from data.Product import Product
from data.Transaction import Transaction


class Order:

    def __init__(self, product: Product, user: User, quantity: int):
        self.order_id = str(uuid.uuid4())
        self.product = product
        self.user = user
        self.quantity = quantity

    def order_to_sql(self):
        return self.order_id, self.user.get_username(), self.product.get_product_id(), self.quantity

    def get_product_title(self):
        return self.product.get_product_name()

    def get_product_id(self):
        return self.product.get_product_id()

    def get_total_price(self):
        return self.product.get_product_price() * self.quantity

    def get_product_image(self):
        return self.product.get_product_image()

    @staticmethod
    def blank_order():
        return Order(Product.blank_product(), None, 0)

    def get_product(self):
        return self.product

    # Getter for quantity
    def get_quantity(self):
        return self.quantity

    # Setter for quantity
    def set_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Order ID: {self.order_id}, Quantity: {self.quantity}, Product ID: {self.product.get_product_id()}"
