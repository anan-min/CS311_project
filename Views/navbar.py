import tkinter as tk


class Navbar(tk.Frame):
    # Define common style properties for all labels
    LABEL_STYLE = {"bg": "#E7AEB2", "fg": "white",
                   "font": ("Arial", 12, "bold")}

    def __init__(self, root, frames):
        super().__init__(root, bg="#E7AEB2")
        self.root = root
        self.frames = frames
        self.config_navbar()

    def config_navbar(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        shop_label = tk.Label(self, text="SHOP", **self.LABEL_STYLE)
        shop_label.config(font=("Arial", 16, "bold"))

        product_label = tk.Label(self, text="PRODUCTS", **self.LABEL_STYLE)
        orders_label = tk.Label(self, text="ORDERS", **self.LABEL_STYLE)
        login_label = tk.Label(self, text="LOGIN", **self.LABEL_STYLE)
        cart_label = tk.Label(self, text="CART", **self.LABEL_STYLE)

        shop_label.grid(row=0, column=0, sticky="news")

        product_label.grid(row=0, column=4, sticky="news")
        orders_label.grid(row=0, column=5, sticky="news")
        login_label.grid(row=0, column=6, sticky="news")
        cart_label.grid(row=0, column=7, sticky="news")
