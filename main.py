import tkinter as tk  
from tkinter import ttk  
import sqlite3

class App:
    def __init__(self, root):
        self.root = root 
        self.session_id = None  

    def create_nav_bar():
        pass 

    def open_main_window():
        pass 

    def open_products_page():
        pass 

    def open_product_page(product_id):
        pass 

    def open_cart_page(cart_id):
        pass 


    def open_payment_page(cart_id):
        pass 

    def open_authentication_page():
        # register 
        # login
        pass 

    def open_profile_page():
        pass 

    def open_orders_page():
        pass 



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()