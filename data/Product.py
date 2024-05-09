class Product:
    def __init__(self, product_id, product_name, product_price, product_description, product_image='images/hirono.jpg', is_blank_product=False):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_image = product_image
        self.is_blank_product = is_blank_product

    # Getter and setter for product_id
    def get_product_id(self):
        return self.product_id

    def set_product_id(self, product_id):
        self.product_id = product_id

    # Getter and setter for product_name
    def get_product_name(self):
        return self.product_name

    def set_product_name(self, product_name):
        self.product_name = product_name

    # Getter and setter for product_price
    def get_product_price(self):
        return self.product_price

    def set_product_price(self, product_price):
        self.product_price = product_price

    # Getter and setter for product_description
    def get_product_description(self):
        return self.product_description

    def set_product_description(self, product_description):
        self.product_description = product_description

    # Getter and setter for product_image
    def get_product_image(self):
        return self.product_image

    def set_product_image(self, product_image):
        self.product_image = product_image

    # Getter and setter for is_blank_product
    def is_blank_product(self):
        return self.is_blank_product

    def set_is_blank_product(self, is_blank_product):
        self.is_blank_product = is_blank_product

    # Static method to create a blank product
    @staticmethod
    def blank_product():
        return Product("None", "No product available", 0, "No product description available", "images/No-Image-Placeholder.png", True)

    # String representation of the Product object
    def __str__(self):
        return f"Product ID: {self.product_id}, Product Name: {self.product_name}, Price: {self.product_price}, Description: {self.product_description}, Image: {self.product_image}, Blank Product: {self.is_blank_product}"
