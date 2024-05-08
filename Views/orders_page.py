from PIL import ImageTk, Image
import tkinter as tk
from data.app_data import App_data
from modules.helper_func import load_and_resize_image


class Orders_page(tk.Frame):
    BG_COLOUR = "#F7F1EE"
    LABEL_STYLE = {
        "font": ("Arial", 10),
        "padx": 10,
        "pady": 10,
        "bg": BG_COLOUR
    }

    def __init__(self, app_data: App_data):
        parent = app_data.get_content_area()
        super().__init__(parent, bg="white")
        self.config_products_page()
        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)
        self.parent = parent
        self.app_data = app_data
        self.config_products_page()
        self.attach_frame_to_parent()

    def config_products_page(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2, 3), weight=4)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_propagate(False)

        self.create_options_button()
        self.create_orders_frame()

    def create_orders_frame(self):
        for i in range(3):
            order_frame = self.create_order_frame()
            order_frame.grid(row=i+1, column=0, columnspan=4,
                             sticky="news", padx=15, pady=15)

    def create_options_button(self):
        options = ["Page 1", "Page 2", "Page 3", "Page 4"]
        selected_option = tk.StringVar()
        selected_option.set(options[0])
        page_button = tk.OptionMenu(
            self, selected_option, *options)
        page_button.configure(
            bg="#F7F1EE", highlightthickness=0, borderwidth=1, height=3, width=25, font=("Arial", 8))
        page_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    def create_order_frame(self):
        order_frame = tk.Frame(self, bg="#F7F1EE")
        order_frame.rowconfigure((0, 1, 2), weight=1)
        order_frame.columnconfigure(0, weight=1)
        order_frame.columnconfigure((1, 2), weight=3)
        order_frame.grid_propagate(False)

        img1 = load_and_resize_image("images/teletubbies.jpeg", (100, 100))
        img_widget = tk.Label(order_frame, image=img1, bg=self.BG_COLOUR)
        img_widget.image = img1

        product_title_label = tk.Label(
            order_frame, text="CRYBABY CHEER UP, BABY! SERIES-Plush Doll",  **self.LABEL_STYLE)
        product_id_label = tk.Label(
            order_frame, text="Product ID: 1234567890", **self.LABEL_STYLE)
        product_price_label = tk.Label(
            order_frame, text="$1050", bg=self.BG_COLOUR, font=("Arial", 15, "bold"), fg="#E7AEB2")

        img_widget.grid(row=0, column=0, rowspan=3,
                        sticky="ew", padx=10, pady=10)
        product_title_label.grid(row=0, column=1, sticky="w")
        product_id_label.grid(row=1, column=1, sticky="w")
        product_price_label.grid(row=2, column=2, sticky="e", padx=10, pady=10)

        return order_frame

    def attach_frame_to_parent(self):
        switch_main_frame(self.parent, self)
