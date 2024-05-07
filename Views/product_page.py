import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
from modules.helper_func import convert_text_to_anchor_left, load_and_resize_image


class Product_page(tk.Frame):

    PRODUCT_INFO = convert_text_to_anchor_left("""
        Brand: POP MART
        Size: About 22cm*14cm*32cm
        Material: 
        Shell:97% Polyester fiber,3% Spandex
        Stuffing:70% Polyester fiber,23%POM,7%PE particles
    """)
    BG_COLOUR = "#F7F1EE"

    def __init__(self, parent, app_data, product_id):
        super().__init__(parent, bg="white")
        self.parent = parent
        self.app_data = app_data
        self.product_id = product_id

        self.configuration()
        self.create_and_place_widgets()
        self.attach_frame_to_parent()

    def configuration(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=5)
        self.grid_propagate(False)
        self.grid(padx=50, pady=(50, 150))

    def create_and_place_widgets(self):
        self.create_and_place_image_frame()
        self.create_and_place_info_frame()

    def create_and_place_image_frame(self):
        image_frame = tk.Frame(self, background="#F7F1EE")
        image_frame.grid(row=0, column=0, sticky="news", padx=10)
        image_frame.pack_propagate(False)

        img = load_and_resize_image("images/fairy.jpeg")
        image_widget = tk.Label(image_frame, image=img)
        image_widget.image = img
        image_widget.pack(fill=tk.BOTH, expand=True)

    def create_and_place_info_frame(self):
        info_frame = tk.Frame(self, background="#F7F1EE")
        info_frame.grid(row=0, column=1, sticky="news")
        info_frame.grid_propagate(False)

        info_frame.grid_rowconfigure((0, 1, 3), weight=1)
        info_frame.grid_rowconfigure(2, weight=3)
        info_frame.columnconfigure((0, 1), weight=1)

        product_title_widget = tk.Label(
            info_frame, text="CRYBABY CHEER UP, BABY! SERIES-Plush Doll", padx=40, pady=20, font=("Arial", 16, "bold"), background=self.BG_COLOUR)
        product_price_widget = tk.Label(
            info_frame, text="$1050", padx=40, pady=10, font=("Arial", 20, "bold"), background=self.BG_COLOUR, foreground="#E7AEB2")
        product_description_widget = tk.Label(
            info_frame, text=self.PRODUCT_INFO, justify=tk.LEFT, padx=40, pady=10, font=("Arial", 12), background=self.BG_COLOUR)

        quantity_button_frame = tk.Frame(
            info_frame, padx=60, pady=30, background=self.BG_COLOUR)
        self.create_quantity_button(quantity_button_frame)

        add_to_cart_button = tk.Button(
            info_frame, text="Add to cart", padx=10, pady=10, borderwidth=0, background="#E7AEB2", foreground="white", font=("Arial", 15, "bold"))

        product_title_widget.grid(row=0, column=0, columnspan=2, sticky="nws")
        product_price_widget.grid(row=1, column=0, columnspan=2, sticky="nws")
        product_description_widget.grid(
            row=2, column=0, columnspan=2, sticky="nws")

        quantity_button_frame.grid(
            row=3, column=0, sticky="news", padx=(0, 10), pady=30)
        add_to_cart_button.grid(
            row=3, column=1, sticky="news", padx=(0, 30), pady=50)

    def create_quantity_button(self, quantity_button_frame):
        # quantity_button_frame.pack_propagate(False)
        minus_button = tk.Button(
            quantity_button_frame, text="-", borderwidth=0, background="#E7AEB2", command=self.decrease_amount)
        amount_label = tk.Label(quantity_button_frame,
                                text="0", justify="center", background="white")
        plus_button = tk.Button(quantity_button_frame,
                                text="+", borderwidth=0, background="#E7AEB2", command=self.increase_amount)

        minus_button.pack(side="left", fill="both", expand=True)
        amount_label.pack(side="left", fill="both", expand=True)
        plus_button.pack(side="left", fill="both", expand=True)

        self.amount_label = amount_label

    def decrease_amount(self):
        current_value = int(self.amount_label["text"])
        if current_value != 0:
            self.amount_label["text"] = str(current_value - 1)

    def increase_amount(self):
        current_value = int(self.amount_label["text"])
        self.amount_label["text"] = str(current_value + 1)

    def attach_frame_to_parent(self):
        self.grid(row=0, column=0, sticky="news")
