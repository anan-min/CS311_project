from PIL import ImageTk, Image
import tkinter as tk
from data.app_data import App_data
from modules.helper_func import load_and_resize_image
from data.Transaction import Transaction


class Orders_page(tk.Frame):
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
        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)
        self.parent = parent
        self.app_data = app_data
        self.config_transactions_page()
        self.attach_frame_to_parent()

    def config_transactions_page(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2, 3), weight=4)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_propagate(False)

        self.create_options_button()
        self.update_transaction_frame()

    def update_transaction_frame(self, page_number=1):

        transactions = self.app_data.get_transactions()
        i_transaction = (page_number - 1) * 3
        self.forget_all_frames()

        for i in range(3):
            transaction__frame = self.create_transaction__frame(
                transactions[i_transaction])
            transaction__frame.grid(row=i+1, column=0, columnspan=4,
                                    sticky="news", padx=15, pady=15)
            i_transaction += 1

    def create_options_button(self):
        transactions = self.app_data.get_transactions()

        num_pages = int(len(transactions) / 3)
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


        self.page_button = page_button

    def on_page_selected(self, option):
        page_number = int(option.split()[1])  # Extract page number
        self.update_transaction_frame(page_number)

    def create_transaction__frame(self, transaction: Transaction):
        transaction__frame = tk.Frame(self, bg="#F7F1EE")
        transaction__frame.rowconfigure((0, 1, 2), weight=1)
        transaction__frame.columnconfigure(0, weight=1)
        transaction__frame.columnconfigure((1, 2), weight=3)
        transaction__frame.grid_propagate(False)

        img1 = load_and_resize_image("images/location.jpg", (100, 100))
        img_widget = tk.Label(transaction__frame,
                              image=img1, bg=self.BG_COLOUR)
        img_widget.image = img1

        transaction_id_label = tk.Label(
            transaction__frame, text=f"transaction id: {transaction.get_transaction_id()}",  **self.LABEL_STYLE)
        transaction_address_label = tk.Label(
            transaction__frame, text=f"address: {transaction.get_address()}", **self.LABEL_STYLE)
        transaction_amount_label = tk.Label(
            transaction__frame, text=f"payment amount {transaction.payment_amount}", **self.LABEL_STYLE)

        img_widget.grid(row=0, column=0, rowspan=3,
                        sticky="ew", padx=10, pady=10)
        transaction_id_label.grid(row=0, column=1, sticky="w")
        transaction_address_label.grid(row=1, column=1, sticky="w")
        transaction_amount_label.grid(
            row=2, column=1, sticky="w")

        return transaction__frame

    def attach_frame_to_parent(self):
        self.app_data.switch_main_frame(self)

    def forget_all_frames(self):
        for widget in self.winfo_children():
            if widget != self.page_button:
                widget.grid_forget()
