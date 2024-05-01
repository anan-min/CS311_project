
import tkinter as tk

class Auth_page(tk.Frame):
    def __init__(self, parent, frames):
        super().__init__(parent)
        self.frames = frames 
        self.config_auth_page()
        self.grid(row=0, column=0, sticky="news")
    
    def config_auth_page(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.grid(padx=30, pady=30)

        for i in range(1):
            for j in range(2):
                label = tk.Label(
                    self, text=f"auth page Row {i}, Col {j}", borderwidth=1, relief="solid")
                label.grid(row=i, column=j, sticky="nsew", padx=20, pady=20)


        # register and login 
                
        def create_login_frame(self):
            pass 


    
