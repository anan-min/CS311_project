from PIL import ImageTk, Image
import tkinter as tk
from modules.app_data import App_data


class Products_page(tk.Frame):
    def __init__(self, parent, app_data: App_data):
        super().__init__(parent, bg="white")
        self.config_products_page()

        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)

        self.parent = parent
        self.app_data = app_data

    def config_products_page(self):
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1, 2), weight=3)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        for i in range(3):
            for j in range(4):
                product_frame = tk.Frame(self, background="red")
                product_frame.pack_propagate()

                raw_img = Image.open("images/fairy.jpeg")
                resized_img = raw_img.resize((400, 400))
                photo_img = ImageTk.PhotoImage(resized_img)

                product_img_widget = tk.Label(
                    product_frame, background="green")
                product_info_frame = tk.Frame(
                    product_frame, background="blue")

                product_img_widget.pack(expand=True, fill="both")
                product_info_frame.pack(expand=True, fill="both")

                product_frame.grid(
                    row=i, column=j, sticky="nsew", padx=20, pady=20)
