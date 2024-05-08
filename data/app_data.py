from data.database import Database
from data.Product import Product
from data.User import User
from data.Order import Order
from data.Product import Product
from data.Transaction import Transaction


class App_data:
    def __init__(self):
        self.frames = {}
        self.database = Database()
        self.current_transaction = Transaction()
        self.current_user = None
        self.current_product = None
        self.content_area = None

    def set_conten_area(self, content_area):
        self.content_area = content_area

    def get_content_area(self):
        return self.content_area

    def is_user_logged_in(self):
        return self.current_user is not None

    def set_current_product(self, product):
        self.current_product = product

    def add_to_cart(self, quantity):
        order = Order(self.current_user,
                      self.current_product, self.current_transaction, quantity)

        self.current_transaction.add_order(order)

    def set_current_user(self, user):
        self.current_user = user
        self.current_transaction.set_user_id(user.get_username())

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

    def add_frame(self, frame):
        self.frames.append(frame)

    def switch_main_frame(self, child_frame):
        content_area = self.content_area
        print(content_area._name)
        # Forget all other child frames
        for frame in content_area.winfo_children():
            if frame != child_frame:
                frame.grid_forget()

        # Grid the selected child frame
        child_frame.grid(row=0, column=0, sticky="news")
