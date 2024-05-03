import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk


class Product_page(tk.Frame):

    PRODUCT_INFO = "Brand: POP MART\nSize: Height about 5-8cm\nMaterial: PVC/ABS/POM/Magnet\nA set contains 12 blind boxes\n(No repeats if you buy a set)\n*Chance to win a secret edition"

    def __init__(self, parent, app_data, product_id):
        super().__init__(parent, bg="white")
        self.app_data = app_data
        self.product_id = product_id
        self.create_product_page(product_id)

    def create_product_page(self, product_id):
        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=5)

        product_info_frame = self.create_product_info_frame()
        product_image_frame = self.create_product_image_frame()

        product_info_frame.grid(row=0, column=1, sticky="news", padx=10)
        product_image_frame.grid(row=0, column=0, sticky="news")

    def create_product_info_frame(self):
        product_info_frame = tk.Frame(
            self, background="#F7F1EE", padx=10, pady=10)
        product_info_frame.grid_rowconfigure((0, 1, 3), weight=1)
        product_info_frame.grid_rowconfigure(2, weight=3)
        product_info_frame.grid_columnconfigure((0, 1), weight=1)

        return product_info_frame

    def create_product_image_frame(self):
        # product_image_frame = tk.Frame(
        #     self, background="red", padx=10, pady=10)
        # product_image_frame.pack_propagate(False)

        # image_path = "images/img_reality.png"
        # raw_image = Image.open(image_path)
        # raw_image = raw_image

        # product_image = ImageTk.PhotoImage(raw_image)
        # product_image_widget = tk.Label(
        #     product_image_frame, image=product_image)
        # product_image_widget.pack(fill="both", expand=False)

        product_image_frame = tk.Frame(
            self, background="white")
        product_image_frame.pack_propagate(False)
        image_path = "images/img_reality.png"

        product_image = PhotoImage(file=image_path)
        product_image = product_image.subsample(2, 2)
        product_image_widget = tk.Label(
            product_image_frame, image=product_image)
        product_image_widget.pack(fill="both", expand=True)

        self.app_data.add_image(product_image)
        return product_image_frame
