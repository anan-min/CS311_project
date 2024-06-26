import tkinter as tk
from modules.helper_func import load_and_resize_image
from Views.main_page import Main_page
from tkinter import messagebox


class Payment_page(tk.Frame):
    BG = "#F7F1EE"

    def __init__(self, app_data):
        parent = app_data.get_content_area()
        super().__init__(parent, bg="white")
        self.app_data = app_data

        self.configuration()
        self.create_and_place_widgets()
        self.attach_frame_to_parent()

    def configuration(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_propagate(False)

    def create_and_place_widgets(self):
        self.create_QR_code_frame()
        self.create_form_frame()

    def create_QR_code_frame(self):
        transaction = self.app_data.current_transaction
        QR_code_frame = tk.Frame(self, background=self.BG)
        QR_code_frame.grid(row=0, column=0, sticky="nsew",
                           padx=30, pady=(30, 150))
        QR_code_frame.grid_propagate()

        QR_code_frame.grid_rowconfigure(0, weight=4)
        QR_code_frame.grid_rowconfigure(1, weight=1)
        QR_code_frame.grid_columnconfigure(0, weight=1)
        QR_code_frame.grid_propagate(False)

        img = load_and_resize_image("images/QR.png", (275, 275))
        image_widget = tk.Label(QR_code_frame, image=img,
                                background=self.BG, padx=40, pady=40)
        image_widget.image = img

        total_price_label = tk.Label(QR_code_frame, text=f"Total price: ${transaction.calculate_subtotal()}", background=self.BG,
                                     padx=30, pady=30, foreground="black", font=("Arial", 15, "bold"))

        image_widget.grid(row=0, column=0, sticky="news")
        total_price_label.grid(
            row=1, column=0, sticky="news", padx=30, pady=(0, 30))

    def create_form_frame(self):
        form_frame = tk.Frame(self, background=self.BG)
        form_frame.grid(row=0, column=1, sticky="nsew",
                        padx=30, pady=(30, 200))
        form_frame.grid_propagate(False)

        form_frame.grid_rowconfigure((0, 5), weight=2)
        form_frame.grid_rowconfigure((1, 2, 3, 4), weight=1)
        form_frame.grid_columnconfigure(0, weight=1)

        payment_heading_label = tk.Label(
            form_frame, text="Payment Information", bg=self.BG, fg="#E7AEB2", font=("Arial", 24, "bold"))

        transfer_amount_title = tk.Label(
            form_frame, text="Transfer Amount", bg=self.BG, fg="black")
        tranfer_amount_entry = tk.Entry(
            form_frame, background="white", fg="black")

        transfer_time_title = tk.Label(
            form_frame, text="Transfer Time", bg=self.BG, fg="black")
        transfer_time_entry = tk.Entry(form_frame, bg="white", fg="black")

        confirm_payment_button = tk.Button(
            form_frame, text="Confirm Purchase", bg="#E7AEB2", fg="white", borderwidth=0, font=("Arial", 16, "bold"), command=self.confirm_payment_button_clicked)

        payment_heading_label.grid(
            row=0, column=0, sticky="news", padx=10, pady=(10, 0))

        transfer_amount_title.grid(
            row=1, column=0, sticky="nws", padx=10, pady=5)
        tranfer_amount_entry.grid(
            row=2, column=0, sticky="news", padx=10, pady=(0, 10))
        transfer_time_title.grid(
            row=3, column=0, sticky="nws", padx=10, pady=5)
        transfer_time_entry.grid(
            row=4, column=0, sticky="news", padx=10, pady=(0, 10))

        confirm_payment_button.grid(
            row=5, column=0, sticky="news", padx=10, pady=30)

        self.transfer_amount_entry = tranfer_amount_entry
        self.transfer_time_entry = transfer_time_entry

    def confirm_payment_button_clicked(self):

        transaction = self.app_data.current_transaction
        transaction.payment_amount = self.transfer_amount_entry.get()
        transaction.payment_time = self.transfer_time_entry.get()

        messagebox.showwarning(
            "Admin : ", "Payment successfully")

        self.app_data.save_transaction()
        Main_page(self.app_data)

    def attach_frame_to_parent(self):
        self.app_data.switch_main_frame(self)
