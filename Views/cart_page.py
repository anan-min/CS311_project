from PIL import ImageTk, Image
import tkinter as tk
from data.app_data import App_data
from modules.helper_func import load_and_resize_image
from data.Product import Product
from data.Order import Order
from Views.payment_page import Payment_page


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
        self.app_data = app_data
        self.parent = parent
        self.order_frames = []

        test = self.test()

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

    def test(self):
        product1 = Product(1, "Hirono", 9.99,
                           "A beautiful flower", "images/fairy.jpeg")
        product2 = Product(2, "Sakura", 12.99,
                           "A delicate cherry blossom", "images/img_reality.jpeg")
        product3 = Product(3, "Momiji", 8.99,
                           "A vibrant maple leaf", "images/hirono.jpg")

        order1 = Order(product1, 1)
        order2 = Order(product2, 3)
        order3 = Order(product3, 2)

        self.app_data.current_transaction.add_order(order1)
        self.app_data.current_transaction.add_order(order2)
        self.app_data.current_transaction.add_order(order3)

        product4 = Product(
            4, "Rose", 11.99, "A classic symbol of love", "images/img_reality.jpeg")
        product5 = Product(
            5, "Sunflower", 10.99, "A bright and cheerful flower", "images/hirono.jpg")
        product6 = Product(
            6, "Tulip", 9.49, "A popular spring flower", "images/img_reality.jpeg")

        order4 = Order(product4, 1)
        order5 = Order(product5, 2)
        order6 = Order(product6, 3)

        self.app_data.current_transaction.add_order(order4)
        self.app_data.current_transaction.add_order(order5)
        # self.app_data.current_transaction.add_order(order6)

    def create_info_frame(self):

        info_frame = tk.Frame(self, bg="#F7F1EE")
        info_frame.grid(row=1, column=2, rowspan=2, columnspan=3,
                        sticky="news", padx=15, pady=15)
        info_frame.rowconfigure((0, 1, 2), weight=1)
        info_frame.rowconfigure(3, weight=5)
        info_frame.columnconfigure((0, 1, 2), weight=1)
        info_frame.grid_propagate(False)
        self.info_frame = info_frame
        self.update_info_frame_widget()

    def update_info_frame_widget(self):
        info_frame = self.info_frame
        transaction = self.app_data.current_transaction
        self.forget_all_info_frame_widgets()

        sub_total_label = tk.Label(
            info_frame, text="sub_total", **self.LABEL_STYLE)
        shipping_label = tk.Label(
            info_frame, text="shipping", **self.LABEL_STYLE)
        total_label = tk.Label(info_frame, text="total", **self.LABEL_STYLE)

        sub_total_amount_label = tk.Label(
            info_frame, text=f"${transaction.calculate_subtotal():.2f}", **self.LABEL_STYLE)
        shipping_amount_label = tk.Label(
            info_frame, text="FREE", **self.LABEL_STYLE)
        total_amount_label = tk.Label(
            info_frame,  text=f"${transaction.calculate_subtotal():.2f}", **self.LABEL_STYLE)

        sub_total_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        shipping_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        total_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        continue_payment_button = tk.Button(info_frame,
                                            text="Continue Payment", font=("Arial", 15, "bold"), borderwidth=0, background="#E7AEB2", foreground="white", command=self.continue_button_clicked)

        sub_total_amount_label.grid(
            row=0, column=2, sticky="e", padx=10, pady=10)
        shipping_amount_label.grid(
            row=1, column=2, sticky="e", padx=10, pady=10)
        total_amount_label.grid(row=2, column=2, sticky="e", padx=10, pady=10)
        continue_payment_button.grid(
            row=3, column=0, columnspan=3, sticky="news", padx=10, pady=10)

    def continue_button_clicked(self):
        Payment_page(self.app_data)
        self.destroy()

    def forget_all_info_frame_widgets(self):
        for widget in self.info_frame.winfo_children():
            widget.grid_forget()

    def create_orders_frame(self, page_number=1):
        self.forget_old_orders_frame()
        orders_to_display = self.get_orders_to_display()

        start_index = (page_number - 1) * 3
        end_index = start_index + 3

        # Display orders for the current page
        for i, order in enumerate(orders_to_display[start_index:end_index]):
            order_frame = self.create_order_frame(order)
            order_frame.grid(row=i+1, column=0, columnspan=2,
                             sticky="news", padx=15, pady=15)

    def forget_old_orders_frame(self):
        for order_frame in self.order_frames:
            order_frame.grid_forget()

    def get_orders_to_display(self):
        transaction = self.app_data.current_transaction
        orders = transaction.get_orders()

        self.page_number = 1

        num_blank_orders = 3 - (len(orders) % 3)
        orders_to_display = orders + [Order.blank_order()] * num_blank_orders

        if len(orders_to_display) == 0:
            orders_to_display = [Order.blank_order()]*3
        return orders_to_display

    def create_options_button(self):
        orders = self.get_orders_to_display()

        num_pages = int(len(orders) / 3)
        options = [f"Page {i+1}" for i in range(num_pages)]

        selected_option = tk.StringVar()
        selected_option.set(options[0])
        selected_option.trace(
            "w", lambda *args: self.on_page_selected(selected_option.get()))

        page_button = tk.OptionMenu(
            self, selected_option, *options)
        page_button.configure(
            bg="#F7F1EE", highlightthickness=0, borderwidth=1, height=3, width=25, font=("Arial", 8))
        page_button.grid(row=0, column=0, padx=15, pady=15, sticky="w")

    def on_page_selected(self, option):
        page_number = int(option.split()[1])  # Extract page number
        self.create_orders_frame(page_number)

    def create_order_frame(self, order: Order):
        order_frame = tk.Frame(self, bg="#F7F1EE")
        order_frame.rowconfigure((0, 1, 2), weight=1)
        order_frame.columnconfigure(0, weight=1)
        order_frame.columnconfigure((1, 2), weight=3)
        order_frame.grid_propagate(False)

        # get image from order
        # get product title, id, and price

        img1 = load_and_resize_image(order.get_product_image(), (100, 100))
        img_widget = tk.Label(order_frame, image=img1)
        img_widget.image = img1

        product_title_label = tk.Label(
            order_frame, text=order.get_product_title(), bg=self.BG_COLOUR)
        product_id_label = tk.Label(
            order_frame, text=f"Product ID:{order.get_product_id()}", bg=self.BG_COLOUR)
        product_price_label = tk.Label(
            order_frame, text=f"${order.get_total_price()}", bg=self.BG_COLOUR, font=("Arial", 15, "bold"), fg="#E7AEB2")

        quantity_button_frame = tk.Frame(
            order_frame, bg="#F7F1EE")
        minus_button = tk.Button(
            quantity_button_frame, text="-", borderwidth=0, bg="#E7AEB2", width=3, height=1, command=lambda: self.decrease_button_clicked(amount_label, order))
        amount_label = tk.Label(quantity_button_frame,
                                text=order.get_quantity(), justify="center", bg="white", width=3, height=1)
        plus_button = tk.Button(quantity_button_frame,
                                text="+", borderwidth=0, bg="#E7AEB2", width=3, height=1, command=lambda: self.increase_button_clicked(amount_label, order))
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

    def decrease_button_clicked(self, label, order):
        quantity = int(label["text"])
        if quantity > 0:
            label["text"] = str(quantity - 1)
            order.set_quantity(quantity - 1)
            self.update_info_frame_widget()

    def increase_button_clicked(self, label, order):
        quantity = int(label["text"])
        if quantity > 0:
            label["text"] = str(quantity + 1)
            order.set_quantity(quantity + 1)
            self.update_info_frame_widget()

    def attach_frame_to_parent(self):
        self.app_data.switch_main_frame(self)
