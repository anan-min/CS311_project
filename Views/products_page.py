from PIL import ImageTk, Image
import tkinter as tk
from data.app_data import App_data
from data.Product import Product
from modules.helper_func import load_and_resize_image


class Products_page(tk.Frame):
    def __init__(self, parent, app_data: App_data):
        super().__init__(parent, bg="white")

        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)

        self.parent = parent
        self.app_data = app_data
        
        self.config_products_page()

    def config_products_page(self):
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1, 2), weight=4)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        products = self.app_data.generate_products()
        num_products = len(products)
        i_product = 0
        blank_product = Product.blank_product()

        for i in range(1, 3):
            for j in range(4):
                if i_product < num_products:
                    product = products[i_product]
                else:
                    product = blank_product
                i_product += 1

                product_frame = tk.Frame(
                    self, background="red")
                product_frame.grid_propagate(False)
                product_frame.grid_rowconfigure(0, weight=5)
                product_frame.grid_rowconfigure(1, weight=1)
                product_frame.grid_columnconfigure(1, weight=1)

                img = load_and_resize_image(product.product_image, (200, 200))

                product_img_widget = tk.Label(
                    product_frame,  image=img)
                product_info_frame = tk.Label(
                    product_frame, text=f"{product.product_name} - {product.product_price}", height=3)

                product_img_widget.image = img

                product_img_widget.grid(row=0, column=0, sticky="news")
                product_info_frame.grid(row=1, column=0, sticky="news")

                product_frame.grid(
                    row=i, column=j, sticky="nsew", padx=30, pady=20)
