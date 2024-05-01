import tkinter as tk
from Views.navbar import Navbar
from Views.contentArea import ContentArea


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def config_root(self):
        self.session_id = None
        self.geometry("1080x720+0+0")
        self.frames = {}
        self.setup_application()

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
        self.navbar.pack(side="top", fill="x")
        self.content_area.pack(side="top", fill="x")

if __name__ == "__main__":
    app = App()
    app.config_root()
    app.mainloop()
