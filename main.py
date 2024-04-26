import tkinter as tk
from tkinter import ttk
import sqlite3


class App:
    def __init__(self, root):
        self.root = root
        self.session_id = None
        self.root.geometry("1080x720+0+0")

        self.setup_application()

    def setup_application(self):
        self.create_nav_bar()
        self.create_content_area()


    def create_nav_bar(self):
        self.nav_bar_frame = tk.Frame(self.root, height=720*.1, bg="#E7AEB2")
        self.nav_bar_frame.pack(side="top", fill="x")


    def create_content_area(self):
        self.content_area_frame = tk.Frame(self.root)
        self.content_area_frame.pack(side="top", fill="both", expand=True)


    def create_frames(self):
        self.products_page = tk.Frame(self.root)
        self.product_page = tk.Frame(self.root)
        self.authentication_page = tk.Frame(self.root)
        self.payment_page = tk.Frame(self.root)
        self.orders_page = tk.Frame(self.root)
        self.cart_page = tk.Frame(self.root)


    






if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
