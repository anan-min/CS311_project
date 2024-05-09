from PIL import ImageTk, Image
import tkinter as tk
from data.app_data import App_data
from modules.helper_func import load_and_resize_image
from Views.product_page import Product_page


class Main_page(tk.Frame):
    def __init__(self, app_data: App_data):
        content_area = app_data.get_content_area()
        super().__init__(content_area, bg="white")
        self.config_products_page()
        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)
        self.app_data = app_data
        self.config_products_page()
        self.attach_frame_to_parent()

    def config_products_page(self):
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_propagate(False)

        for i in range(2):
            for j in range(2):
                label = tk.Label(
                    self, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

        img1 = load_and_resize_image(
            "images/labubu.png", (520, 520))  # 9
        img2 = load_and_resize_image(
            "images/donald_cover3.webp", (480, 480))  # 5
        img3 = load_and_resize_image(
            "images/lilios_cover.webp", (480, 300))  # 11

        first_img_widget = tk.Label(self, image=img1)
        first_img_widget.image = img1
        second_img_widget = tk.Label(self, image=img2)
        second_img_widget.image = img2
        third_img_widget = tk.Label(self, image=img3)
        third_img_widget.image = img3

        first_img_widget.grid(row=0, column=0, rowspan=2,
                              sticky="news", padx=20, pady=20)
        second_img_widget.grid(
            row=0, column=1, sticky="news", padx=20, pady=20)
        third_img_widget.grid(row=1, column=1, sticky="news", padx=20, pady=20)

        first_img_widget.bind("<Button-1>", self.on_image_click_1)
        second_img_widget.bind("<Button-1>", self.on_image_click_2)
        third_img_widget.bind("<Button-1>", self.on_image_click_3)

    def on_image_click_1(self, event):
        product = self.app_data.get_product(9)
        self.app_data.current_product = product

        product_page = Product_page(self.app_data)
        product_page.attach_frame_to_parent()


    def on_image_click_2(self, event):
        product = self.app_data.get_product(5)
        self.app_data.current_product = product

        product_page = Product_page(self.app_data)
        product_page.attach_frame_to_parent()


    def on_image_click_3(self, event):
        product = self.app_data.get_product(11)
        self.app_data.current_product = product
        product_page = Product_page(self.app_data)
        product_page.attach_frame_to_parent()


    def attach_frame_to_parent(self):
        self.app_data.switch_main_frame(self)
