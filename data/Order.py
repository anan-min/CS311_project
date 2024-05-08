import uuid
from data.User import User
from data.Product import Product
from data.Transaction import Transaction


class Order:
    def __init__(self, order_id=str(uuid.uuid4()), user_id=None, product_id=None, transaction_id=None, quantity=1):
        self.order_id = order_id
        self.user_id = user_id
        self.product_id = product_id
        self.transaction_id = transaction_id
        self.quantity = quantity

    def __init__(self, current_user: User, current_product: Product, current_transaction: Transaction, quantity: int):
        self.order_id = str(uuid.uuid4())
        self.user_id = current_user.get_username()
        self.product_id = current_product.get_product_id()
        self.transaction_id = current_transaction.get_transaction_id()
        self.quantity = quantity
    # Getter for order_id

    def get_order_id(self):
        return self.order_id

    # Setter for order_id
    def set_order_id(self, order_id):
        self.order_id = order_id

    # Getter for user_id
    def get_user_id(self):
        return self.user_id

    # Setter for user_id
    def set_user_id(self, user_id):
        self.user_id = user_id

    # Getter for product_id
    def get_product_id(self):
        return self.product_id

    # Setter for product_id
    def set_product_id(self, product_id):
        self.product_id = product_id

    # Getter for quantity
    def get_quantity(self):
        return self.quantity

    # Setter for quantity
    def set_quantity(self, quantity):
        self.quantity = quantity

    # Getter for transaction_id
    def get_transaction_id(self):
        return self.transaction_id

    # Setter for transaction_id
    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    # String representation of the Order object
    def __str__(self):
        return f"Order ID: {self.order_id}, User ID: {self.user_id}, Product ID: {self.product_id}"