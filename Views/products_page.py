from PIL import ImageTk, Image
import tkinter as tk
from data.app_data import App_data
from data.Product import Product
from Views.product_page import Product_page
from modules.helper_func import load_and_resize_image


class Products_page(tk.Frame):
    def __init__(self, app_data: App_data):
        parent = app_data.get_content_area()
        super().__init__(parent, bg="white")

        self.parent = parent
        self.app_data = app_data

        self.config_products_page()
        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)

    def config_products_page(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2), weight=6)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_propagate(False)
        self.pack_propagate(False)

        options = ["Page 1", "Page 2", "Page 3", "Page 4"]
        selected_option = tk.StringVar()
        selected_option.set(options[0])
        page_button = tk.OptionMenu(
            self, selected_option, *options)
        page_button.configure(
            bg="#F7F1EE", highlightthickness=0, borderwidth=1, height=3, width=25, font=("Arial", 8))
        page_button.grid(row=0, column=0, columnspan=4,
                         padx=(30, 10), sticky="w")

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
                    self)

                product_frame.grid_propagate(False)
                product_frame.grid_rowconfigure(0, weight=5)
                product_frame.grid_rowconfigure(1, weight=1)
                product_frame.grid_columnconfigure(1, weight=1)
                product_frame.grid_propagate(False)

                img = load_and_resize_image(product.product_image, (210, 210))

                product_img_widget = tk.Label(
                    product_frame,  image=img)
                product_info_frame = tk.Label(
                    product_frame, text=f"{product.product_name} - {product.product_price}", height=3, bg="#F7F1EE", font=("Arial", 10))

                product_img_widget.image = img

                product_img_widget.grid(row=0, column=0, sticky="news")
                product_info_frame.grid(row=1, column=0, sticky="news")

                product_img_widget.bind(
                    "<Double-1>", lambda event, product=product: self.on_product_click(product))
                product_info_frame.bind(
                    "<Double-1>", lambda event, product=product: self.on_product_click(product))

                product_frame.grid(
                    row=i, column=j, sticky="nsew", padx=25, pady=20)

    def on_product_click(self, product):
        print("button is clicked")
        self.app_data.set_current_product(product)
        product_page = Product_page(self, self.app_data)
