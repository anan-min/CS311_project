from PIL import ImageTk, Image
import tkinter as tk
from modules.app_data import App_data
from modules.helper_func import load_and_resize_image, switch_main_frame


class Main_page(tk.Frame):
    def __init__(self, parent, app_data: App_data):
        super().__init__(parent, bg="white")
        self.config_products_page()

        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)

        self.parent = parent
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

        img1 = load_and_resize_image("images/teletubbies.jpeg", (540, 540))
        img2 = load_and_resize_image("images/teletubbies.jpeg", (470, 470))
        img3 = load_and_resize_image("images/teletubbies.jpeg", (470, 470))

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

    def attach_frame_to_parent(self):
        switch_main_frame(self.parent, self)
