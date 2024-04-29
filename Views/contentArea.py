import tkinter as tk
from modules.helper_func import switch_main_frame


class ContentArea(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.config_content_area()

    def config_content_area(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def get_frames(self):
        self.frames = {}
        page_names = ["main_page", "products_page", "product_page",
                      "authentication_page", "payment_page",
                      "orders_page", "cart_page"]

        for page_name in page_names:
            frame = tk.Frame(self)
            self.frames[page_name] = frame

        self.frames["content_area"] = self

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

        # self.switch_main_frame(self.content_area_frame, products_page)

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

        # self.switch_main_frame(self.content_area_frame, main_page)

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

        # self.switch_main_frame(self.content_area_frame, product_page)

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

        # self.switch_main_frame(self.content_area_frame, payment_page)

    def create_authentication_page(self):
        auth_page = self.frames["authentication_page"]
        auth_page.grid_rowconfigure(0, weight=1)
        auth_page.grid_columnconfigure(0, weight=2)
        auth_page.grid_columnconfigure(1, weight=3)
        auth_page.grid(padx=30, pady=30)

        for i in range(1):
            for j in range(2):
                label = tk.Label(
                    auth_page, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

        # self.switch_main_frame(self.content_area_frame, auth_page)
