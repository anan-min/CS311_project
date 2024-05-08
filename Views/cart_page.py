from PIL import ImageTk, Image
import tkinter as tk
from data.app_data import App_data
from modules.helper_func import load_and_resize_image


class Cart_page(tk.Frame):
    BG_COLOUR = "#F7F1EE"
    LABEL_STYLE = {
        "font": ("Arial", 10, "bold"),
        "padx": 10,
        "pady": 10,
        "bg": BG_COLOUR
    }

    def __init__(self, app_data: App_data):
        parent = app_data.get_content_area()
        super().__init__(parent, bg="white")
        self.config_products_page()
        self.parent = parent
        self.app_data = app_data
        self.config_products_page()
        self.attach_frame_to_parent()

    def config_products_page(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2, 3), weight=2)
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_propagate(False)

        self.create_options_button()
        self.create_orders_frame()
        self.create_info_frame()

    def create_info_frame(self):
        info_frame = tk.Frame(self, bg="#F7F1EE")
        info_frame.grid(row=1, column=2, rowspan=2, columnspan=3,
                        sticky="news", padx=15, pady=15)
        info_frame.rowconfigure((0, 1, 2), weight=1)
        info_frame.rowconfigure(3, weight=5)
        info_frame.columnconfigure((0, 1, 2), weight=1)
        info_frame.grid_propagate(False)

        sub_total_label = tk.Label(
            info_frame, text="sub_total", **self.LABEL_STYLE)
        shipping_label = tk.Label(
            info_frame, text="shipping", **self.LABEL_STYLE)
        total_label = tk.Label(info_frame, text="total", **self.LABEL_STYLE)

        sub_total_amount_label = tk.Label(
            info_frame, text="$1235", **self.LABEL_STYLE)
        shipping_amount_label = tk.Label(
            info_frame, text="FREE", **self.LABEL_STYLE)
        total_amount_label = tk.Label(
            info_frame,  text="$1235", **self.LABEL_STYLE)

        sub_total_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        shipping_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        total_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        continue_payment_button = tk.Button(info_frame,
                                            text="Continue Payment", font=("Arial", 15, "bold"), borderwidth=0, background="#E7AEB2", foreground="white")

        sub_total_amount_label.grid(
            row=0, column=2, sticky="e", padx=10, pady=10)
        shipping_amount_label.grid(
            row=1, column=2, sticky="e", padx=10, pady=10)
        total_amount_label.grid(row=2, column=2, sticky="e", padx=10, pady=10)
        continue_payment_button.grid(
            row=3, column=0, columnspan=3, sticky="news", padx=10, pady=10)

    def create_orders_frame(self):
        for i in range(3):
            order_frame = self.create_order_frame()
            order_frame.grid(row=i+1, column=0, columnspan=2,
                             sticky="news", padx=15, pady=15)

    def create_options_button(self):
        options = ["Page 1", "Page 2", "Page 3", "Page 4"]
        selected_option = tk.StringVar()
        selected_option.set(options[0])
        page_button = tk.OptionMenu(
            self, selected_option, *options)
        page_button.configure(
            bg="#F7F1EE", highlightthickness=0, borderwidth=1, height=3, width=25, font=("Arial", 8))
        page_button.grid(row=0, column=0, padx=15, pady=15, sticky="w")

    def create_order_frame(self):
        order_frame = tk.Frame(self, bg="#F7F1EE")
        order_frame.rowconfigure((0, 1, 2), weight=1)
        order_frame.columnconfigure(0, weight=1)
        order_frame.columnconfigure((1, 2), weight=3)
        order_frame.grid_propagate(False)

        img1 = load_and_resize_image("images/teletubbies.jpeg", (100, 100))
        img_widget = tk.Label(order_frame, image=img1)
        img_widget.image = img1

        product_title_label = tk.Label(
            order_frame, text="CRYBABY CHEER UP, BABY! SERIES-Plush Doll", bg=self.BG_COLOUR)
        product_id_label = tk.Label(
            order_frame, text="Product ID: 1234567890", bg=self.BG_COLOUR)
        product_price_label = tk.Label(
            order_frame, text="$1050", bg=self.BG_COLOUR, font=("Arial", 15, "bold"), fg="#E7AEB2")

        quantity_button_frame = tk.Frame(
            order_frame, bg="#F7F1EE")
        minus_button = tk.Button(
            quantity_button_frame, text="-", borderwidth=0, bg="#E7AEB2", width=3, height=1)
        amount_label = tk.Label(quantity_button_frame,
                                text="0", justify="center", bg="white", width=3, height=1)
        plus_button = tk.Button(quantity_button_frame,
                                text="+", borderwidth=0, bg="#E7AEB2", width=3, height=1)
        minus_button.pack(side="left", fill="both", expand=True)
        amount_label.pack(side="left", fill="both", expand=True)
        plus_button.pack(side="left", fill="both", expand=True)

        img_widget.grid(row=0, column=0, rowspan=3,
                        sticky="w", padx=10, pady=10)
        product_title_label.grid(row=0, column=1, sticky="w")
        product_id_label.grid(row=1, column=1, sticky="w")
        quantity_button_frame.grid(row=2, column=1, sticky="w")
        product_price_label.grid(row=2, column=2, sticky="w")

        return order_frame

    def attach_frame_to_parent(self):
        self.app_data.switch_main_frame(self)
