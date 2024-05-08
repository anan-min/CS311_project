import tkinter as tk
from Views.auth_page import Auth_page
from Views.product_page import Product_page
from Views.payment_page import Payment_page
from Views.products_page import Products_page
from Views.main_page import Main_page
from Views.cart_page import Cart_page
from Views.orders_page import Orders_page
from data.app_data import App_data


class ContentArea(tk.Frame):
    def __init__(self, root, app_data: App_data):
        super().__init__(root, bg="white")
        self.root = root
        self.app_data = app_data
        self.app_data.content_area = self
        self.config_content_area()

    def config_content_area(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.create_frames()

    def create_frames(self):
        Main_page(self.app_data)

    def create_products_page(self):
        products_page = self.frames["product_page"]
        products_page.grid_rowconfigure((0), weight=1)
        products_page.grid_rowconfigure((1, 2), weight=3)
        products_page.grid_columnconfigure((0, 1, 2, 3), weight=1)

        for i in range(3):
            for j in range(4):
                label = tk.Label(
                    products_page, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

    def create_main_page(self):
        main_page = self.frames["main_page"]
        main_page.grid_rowconfigure((0, 1), weight=1)
        main_page.grid_columnconfigure(0, weight=2)
        main_page.grid_columnconfigure(1, weight=1)

        for i in range(2):
            for j in range(2):
                label = tk.Label(
                    main_page, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

    def create_product_page(self):
        product_page = self.frames["product_page"]
        product_page.grid_rowconfigure(0, weight=1)
        product_page.grid_columnconfigure(0, weight=1)
        product_page.grid_columnconfigure(1, weight=2)
        product_page.grid(padx=30, pady=30)

        for i in range(1):
            for j in range(2):
                label = tk.Label(
                    product_page, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

    def create_payment_page(self):
        payment_page = self.frames["payment_page"]
        payment_page.grid_rowconfigure(0, weight=1)
        payment_page.grid_columnconfigure(0, weight=1)
        payment_page.grid_columnconfigure(1, weight=2)
        payment_page.grid(padx=30, pady=(30, 120))

        for i in range(1):
            for j in range(2):
                label = tk.Label(
                    payment_page, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)
