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
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=5)
        self.grid_propagate(False)
        self.grid(padx=50, pady=60)

    def create_and_place_widgets(self):
        image_frame = tk.Frame(self, background="#F7F1EE")
        info_frame = tk.Frame(self, background="#F7F1EE")
        image_frame.pack_propagate(False)

        image_frame.grid(row=0, column=0, sticky="news", padx=10)
        info_frame.grid(row=0, column=1, sticky="news", padx=10)

        raw_img = Image.open("images/fairy.jpeg")
        resized_img = raw_img.resize((520, 520))
        img = ImageTk.PhotoImage(resized_img)
        image_widget = tk.Label(image_frame, image=img)
        image_widget.image = img
        image_widget.pack(fill=tk.BOTH, expand=True)

    def attach_frame_to_parent(self):
        self.grid(row=0, column=0, sticky="news")
