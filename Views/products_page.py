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
        self.product_frames = []
        self.config_products_page()
        self.attach_frame_to_parent()

    def config_products_page(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2), weight=7)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_propagate(False)
        self.pack_propagate(False)

        self.create_options_button()
        self.update_products_frames()


    def create_options_button(self):
        products = self.app_data.get_products()

        num_pages = int(len(products) / 8)
        options = [f"Page {i+1}" for i in range(num_pages)]

        selected_option = tk.StringVar()
        selected_option.set(options[0])
        selected_option.trace(
            "w", lambda *args: self.on_page_selected(selected_option.get()))

        page_button = tk.OptionMenu(
            self, selected_option, *options)
        page_button.configure(
            bg="#F7F1EE", highlightthickness=0, borderwidth=1, height=3, width=25, font=("Arial", 8))
        page_button.grid(row=0, column=0, padx=15,
                         pady=15, sticky="w", columnspan=4)

        self.page_button = page_button

    def on_page_selected(self, option):
        page_number = int(option.split()[1])  # Extract page number
        self.update_products_frames(page_number)

    def get_products_to_display(self):
        products = self.app_data.get_products()

        num_blank_products = 8 - (len(products) %
                                  8) if len(products) % 8 != 0 else 0
        products_to_display = products + \
            [Product.blank_product()] * num_blank_products

        if len(products_to_display) < 8:
            products_to_display += [Product.blank_product()] * \
                (8 - len(products_to_display))

        return products_to_display

    def update_products_frames(self, page_number=1):
        products = self.get_products_to_display()
        self.forget_all_products_frame()
        self.grid_propagate(False)

        i_product = (page_number - 1) * 8

        for i in range(1, 3):
            for j in range(4):
                product_frame = self.create_product_frame(products[i_product])
                product_frame.grid_propagate(False)
                product_frame.grid(
                    row=i, column=j, sticky="nsew", padx=25, pady=10)
                self.product_frames.append(product_frame)
                i_product += 1

    def create_product_frame(self, product: Product):
        product_frame = tk.Frame(self)

        product_frame.grid_propagate(False)
        product_frame.grid_rowconfigure(0, weight=6)
        product_frame.grid_rowconfigure(1, weight=1)
        product_frame.grid_columnconfigure(1, weight=1)
        product_frame.grid_propagate(False)

        img = load_and_resize_image(product.product_image, (350, 350))

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

        return product_frame

    def forget_old_products(self):
        for product_frame in self.product_frames:
            product_frame.grid_forget()

    def on_product_click(self, product):
        self.app_data.set_current_product(product)
        Product_page(self.app_data)

    def attach_frame_to_parent(self):
        self.app_data.switch_main_frame(self)

    def forget_all_products_frame(self):
        for widget in self.winfo_children():
            if widget != self.page_button:
                widget.grid_forget()
