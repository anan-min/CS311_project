import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
from modules.helper_func import convert_text_to_anchor_left


class Product_page(tk.Frame):

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
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=5)
        self.grid_propagate(False)
        self.grid(padx=30, pady=30)

    
    def create_and_place_widgets(self):
        for i in range(1):
            for j in range(2):
                label = tk.Label(
                    self, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid", font=("Helvetica", 100))
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)
    
    def attach_frame_to_parent(self):
        self.grid(row=0, column=0, sticky="news")


