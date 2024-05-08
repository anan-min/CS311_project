
class Product:
    def __init__(self, product_id, product_name, product_price, product_description, product_image='images/hirono.jpg', is_blank_product=False):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_image = product_image
        self.is_blank_product = False

    @staticmethod
    def blank_product():
        return Product(None, "No product available", 0, "No product description available", "images/No-Image-Placeholder.png", True)
