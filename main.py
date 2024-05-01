import tkinter as tk
from Views.navbar import Navbar
from Views.contentArea import ContentArea
from modules.database import Database


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def config_root(self):
        self.session_id = None
        # self.db = Database()
        self.geometry("1080x720+0+0")
        self.frames = {}
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=9)
        self.grid_columnconfigure(0, weight=1)

        self.setup_base_template()

    def setup_base_template(self):
        self.create_content_area()
        self.create_navbar()
        self.attach_frames()

    def create_navbar(self):
        navbar = Navbar(self, self.frames)
        self.navbar = navbar

    def create_content_area(self):
        content_area = ContentArea(self)
        self.frames = content_area.get_frames()
        self.content_area = content_area

    def attach_frames(self):
        self.navbar.grid(row=0, column=0, sticky="news")
        self.content_area.grid(row=1, column=0, sticky="news")


if __name__ == "__main__":
    app = App()
    app.config_root()
    app.mainloop()
