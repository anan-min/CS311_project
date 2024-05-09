import tkinter as tk
from Views.auth_page import Auth_page
from Views.product_page import Product_page
from Views.payment_page import Payment_page
from Views.products_page import Products_page
from Views.main_page import Main_page
from Views.cart_page import Cart_page
from Views.orders_page import Orders_page
from data.app_data import App_data


class ContentArea(tk.Frame):
    def __init__(self, root, app_data: App_data):
        super().__init__(root, bg="white")
        self.root = root
        self.app_data = app_data
        self.app_data.content_area = self
        self.config_content_area()

    def config_content_area(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.create_frames()

    def create_frames(self):
        Auth_page(self.app_data)


 
