import tkinter as tk  
from tkinter import messagebox
from PIL import Image, ImageTk


class Product_page(tk.Frame):

    def __init__(self, parent, app_data, product_id):
        super().__init__(parent, bg="white")
        self.app_data = app_data
        self.product_id = product_id
        self.create_product_page(product_id)


    def create_product_page(self, product_id):
        self.grid(row=0, column=0, sticky="news", padx=30, pady=30)

        self.remove_all_widgets()

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=5)
        self.grid(padx=30, pady=30)

        for i in range(1):
            for j in range(2):
                label = tk.Label(
                    self, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

        # product_image_frame 
        # product_info_frame 
        product_info_frame = self.create_product_info_frame(product_id)
        product_image_widget = self.create_product_image_widget(product_id)

    def create_product_info_frame(self, product_id):
        product_info_frame = tk.Frame(self, background="#F7F1EE")
        product_info_frame.grid(row=0, column=1, sticky="news", padx=20, pady=20)  


            
    def create_product_image_widget(self, product_id):


        raw_image = i

        product_image = tk.PhotoImage(file=image_path)
        self.app_data.add_image(product_image)
        product_img_widget = tk.Label(self, image=product_img)
        product_img_widget.grid(row=0, column=0,sticky="news", padx=20, pady=20)



    def remove_all_widgets(self):
        pass 
