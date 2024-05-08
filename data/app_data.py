from data.database import Database
from data.Product import Product


class App_data:
    def __init__(self):
        self.frames = {}
        self.database = Database()
        self.current_user = None
        self.images = []

    def generate_products(self):
        products = []

        for i in range(4):
            product_id = i + 1
            product_name = f"Product {product_id}"
            product_price = 10 + i  # Just an example for price, you can use any logic here
            product_description = f"This is product {product_id}"
            products.append(Product(product_id, product_name,
                            product_price, product_description))
        return products
            
            

    def add_frame(self, name, frame):
        self.frames[name] = frame

    def add_frames(self, names, frames):
        if len(names) != len(frames):
            raise ValueError(
                "Names and frames lists must have the same length")

        for name, frame in zip(names, frames):
            self.frames[name] = frame

    def get_frame(self, frame_name):
        return self.frames.get(frame_name)

    def get_database(self):
        return self.database

    def get_current_user(self):
        return self.current_user

    def close_connection(self):
        self.database.close_connection()

    def add_image(self, image):
        self.images.append(image)
