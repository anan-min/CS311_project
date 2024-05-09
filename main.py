import tkinter as tk
from Views.navbar import Navbar
from Views.contentArea import ContentArea
from data.database import Database
from data.app_data import App_data


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def config_app(self):
        self.app_data = App_data()
        self.geometry("1080x720+0+0")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=9)
        self.grid_columnconfigure(0, weight=1)

        self.setup_base_template()

    def setup_base_template(self):
        self.create_content_area()
        self.create_navbar()
        self.attach_frames()

    def create_navbar(self):
        navbar = Navbar(self, self.app_data)
        self.navbar = navbar

    def create_content_area(self):
        content_area = ContentArea(self, self.app_data)
        content_area._name = "content_area"
        self.content_area = content_area

    def attach_frames(self):
        self.navbar.grid(row=0, column=0, sticky="news")
        self.content_area.grid(row=1, column=0, sticky="news")

    def close_database(self):
        self.app_data.close_connection()


if __name__ == "__main__":
    app = App()
    app.config_app()
    app.mainloop()
    app.close_database()

    
# if __name__ == "__main__":
#     db = Database()
#     transactions = db.get_transactions()

#     for transaction in transactions:
#         print(transaction)

