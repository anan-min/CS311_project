import tkinter as tk
from Views.auth_page import Auth_page


class Navbar(tk.Frame):
    LABEL_STYLE = {"bg": "#E7AEB2", "fg": "white",
                   "font": ("Arial", 12, "bold")}

    def __init__(self, parent, app_data):
        super().__init__(parent, bg="#E7AEB2")
        self.parent = parent
        self.app_data = app_data
        self.config_navbar()

    def config_navbar(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        shop_label = tk.Label(self, text="SHOP", **self.LABEL_STYLE)
        shop_label.config(font=("Arial", 20, "bold"))

        product_label = tk.Label(self, text="PRODUCTS", **self.LABEL_STYLE, )
        orders_label = tk.Label(self, text="ORDERS", **self.LABEL_STYLE)
        login_label = tk.Label(self, text="LOGIN", **self.LABEL_STYLE)
        cart_label = tk.Label(self, text="CART", **self.LABEL_STYLE)

        shop_label.grid(row=0, column=0, sticky="news")

        product_label.grid(row=0, column=4, sticky="news")
        orders_label.grid(row=0, column=5, sticky="news")
        login_label.grid(row=0, column=6, sticky="news")
        cart_label.grid(row=0, column=7, sticky="news")

        login_label.bind("<Button-1>", self.switch_to_login_page)

    def switch_to_login_page(self, event):
        auth_page = Auth_page(self.app_data)
