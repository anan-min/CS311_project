from PIL import ImageTk, Image
import tkinter as tk
from modules.app_data import App_data
from modules.helper_func import load_and_resize_image


class Products_page(tk.Frame):
    def __init__(self, parent, app_data: App_data):
        super().__init__(parent, bg="white")
        self.config_products_page()

        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)

        self.parent = parent
        self.app_data = app_data

    def config_products_page(self):
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1, 2), weight=4)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        for i in range(1, 3):
            for j in range(4):
                product_frame = tk.Frame(
                    self, background="red")
                product_frame.grid_propagate(False)
                product_frame.grid_rowconfigure(0, weight=5)
                product_frame.grid_rowconfigure(1, weight=1)
                product_frame.grid_columnconfigure(1, weight=1)

                img = load_and_resize_image("images/fairy.jpeg", (200, 200))

                product_img_widget = tk.Label(
                    product_frame,  image=img)
                product_info_frame = tk.Label(
                    product_frame, text="this is a price", height=3)

                product_img_widget.image = img

                product_img_widget.grid(row=0, column=0, sticky="news")
                product_info_frame.grid(row=1, column=0, sticky="news")

                product_frame.grid(
                    row=i, column=j, sticky="nsew", padx=30, pady=20)
