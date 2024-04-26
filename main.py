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
        self.create_frames()

    def create_nav_bar(self):
        nav_bar_frame = tk.Frame(self.root, height=720*.1, bg="#E7AEB2")
        nav_bar_frame.pack(side="top", fill="x")
        self.nav_bar_frame = nav_bar_frame

    def create_content_area(self):
        content_area_frame = tk.Frame(self.root)
        content_area_frame.pack(side="top", fill="both", expand=True)
        self.content_area_frame = content_area_frame

    def create_frames(self):
        content_area_frame = self.content_area_frame
        content_area_frame.grid_rowconfigure(0, weight=1)
        content_area_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        page_names = ["main_page", "products_page", "product_page",
                      "authentication_page", "payment_page",
                      "orders_page", "cart_page"]

        for name in page_names:
            frame = tk.Frame(content_area_frame)
            self.frames[name] = frame

    def switch_main_frame(self, parent_frame, child_frame):
        # Forget all other child frames
        for frame in parent_frame.winfo_children():
            if frame != child_frame:
                frame.grid_forget()

        # Grid the selected child frame
        child_frame.grid(row=0, column=0, sticky="news")

    def create_products_page(self):
        products_page = self.frames["product_page"]
        products_page.grid_rowconfigure((0), weight=1)
        products_page.grid_rowconfigure((1, 2), weight=3)
        products_page.grid_columnconfigure((0, 1, 2, 3), weight=1)

        for i in range(3):
            for j in range(4):
                label = tk.Label(
                    products_page, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

        # self.switch_main_frame(self.content_area_frame, products_page)

    def create_main_page(self):
        main_page = self.frames["main_page"]
        main_page.grid_rowconfigure((0, 1), weight=1)
        main_page.grid_columnconfigure(0, weight=2)
        main_page.grid_columnconfigure(1, weight=1)

        for i in range(2):
            for j in range(2):
                label = tk.Label(
                    main_page, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

        # self.switch_main_frame(self.content_area_frame, main_page)

    def create_product_page(self):
        product_page = self.frames["product_page"]
        product_page.grid_rowconfigure(0, weight=1)
        product_page.grid_columnconfigure(0, weight=1)
        product_page.grid_columnconfigure(1, weight=2)
        product_page.grid(padx=30, pady=30)

        for i in range(1):
            for j in range(2):
                label = tk.Label(
                    product_page, text=f"Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)

        # self.switch_main_frame(self.content_area_frame, product_page)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
