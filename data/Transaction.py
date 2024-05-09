import uuid


class Transaction:
    def __init__(self, transaction_id=str(uuid.uuid4()), user_id=None, transaction_status=None, payment_time=None, payment_amount=None):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.transaction_status = transaction_status
        self.payment_time = payment_time
        self.payment_amount = payment_amount
        self.orders = []

    def calculate_subtotal(self):
        subtotal = 0
        for order in self.orders:
            subtotal += order.get_product().get_product_price() * order.get_quantity()
        return subtotal

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def __str__(self):
        return f"Transaction(transaction_id={self.transaction_id}, user_id={self.user_id}, transaction_status={self.transaction_status}, payment_time={self.payment_time}, payment_amount={self.payment_amount}, orders={self.orders})"

    def get_transaction_id(self):
        return self.transaction_id

    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_transaction_status(self):
        return self.transaction_status

    def set_transaction_status(self, transaction_status):
        self.transaction_status = transaction_status

    def get_payment_time(self):
        return self.payment_time

    def set_payment_time(self, payment_time):
        self.payment_time = payment_time

    def get_payment_amount(self):
        return self.payment_amount

    def set_payment_amount(self, payment_amount):
        self.payment_amount = payment_amount
