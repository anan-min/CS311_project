import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
from modules.helper_func import convert_text_to_anchor_left


class Product_page(tk.Frame):

    PRODUCT_INFO = convert_text_to_anchor_left("""
            Brand: POP MART
            Size: Height about 5-8cm
            Material: PVC/ABS/POM/Magnet
            A whole set contains 12 blind boxes
            (There is no repeated figurine if you buy a whole set)
            *A certain chance to win a secret edition
    """)

    def __init__(self, parent, app_data, product_id):
        super().__init__(parent, bg="white")
        self.app_data = app_data
        self.product_id = product_id
        self.create_product_page(product_id)

    def create_product_page(self, product_id):
        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=50)
        self.grid_columnconfigure(1, weight=4)

        self.create_product_info_frame()
        self.create_product_image_frame()

    def create_product_info_frame(self):
        product_info_frame = tk.Frame(
            self, background="#F7F1EE", padx=10, pady=10)
        product_info_frame.grid(
            row=0, column=1, sticky="news", padx=10, pady=30)

        product_info_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        product_info_frame.grid_columnconfigure(0, weight=1)

        product_title_label = tk.Label(
            product_info_frame, text="SKULLPANDA Image Of Reality Series Figures", font=("Arial", 16, "bold"), bg="#F7F1EE")
        product_title_label.grid(
            row=0, column=0, sticky="nws", padx=20, pady=20)

        product_price_label = tk.Label(
            product_info_frame, text="THB 380", font=("Arial", 18, "normal"), bg="#F7F1EE")
        product_price_label.grid(
            row=1, column=0, sticky="nws", padx=20, pady=20)

        product_content_label = tk.Label(
            product_info_frame, text=self.PRODUCT_INFO, font=("Arial", 10, "bold"), bg="#F7F1EE", justify="left")
        product_content_label.grid(
            row=2, column=0, sticky="nws", padx=20, pady=20)

        add_to_cart_button = tk.Button(product_info_frame, text="add to cart")
        add_to_cart_button.grid(row=3, column=0, sticky="w", padx=20, pady=20)

    def create_product_image_frame(self):
        product_image_frame = tk.Frame(
            self, background="white")
        product_image_frame.grid(
            row=0, column=0, sticky="news", padx=10, pady=30)

        product_image_frame.pack_propagate(False)
        image_path = "images/img_reality.png"

        product_image = PhotoImage(file=image_path)
        product_image = product_image.subsample(2, 2)
        product_image_widget = tk.Label(
            product_image_frame, image=product_image)
        product_image_widget.pack(fill="both", expand=True)

        self.app_data.add_image(product_image)
        return product_image_frame
