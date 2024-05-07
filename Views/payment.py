import tkinter as tk


class Product_page(tk.Frame):
    def __init__(self, parent, app_data):
        self.parent = parent 
        self.app_data = app_data

        self.configuration()
        self.create_and_place_widgets()
        self.attach_frame_to_parent()

    def configuration(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid(padx=30, pady=(30, 120))

    def create_and_place_widgets(self):
        for i in range(1):
            for j in range(2):
                label = tk.Label(
                    self, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

    def attach_frame_to_parent():
        pass
