
import tkinter as tk


class Auth_page(tk.Frame):
    LABEL_STYLE = {"bg": "#E7AEB2", "fg": "white",
                   "font": ("Arial", 12, "bold")}

    def __init__(self, parent, frames):
        super().__init__(parent, bg="white")
        self.frames = frames
        self.config_auth_page()
        self.grid(row=0, column=0, sticky="news")

    def config_auth_page(self):
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.grid(padx=30, pady=30)
        self.setup_login_frame()
        self.setup_register_frame()

    def setup_login_frame(self):
        login_frame = tk.Frame(self, bg="#F7F1EE")
        login_frame.grid(row=0, column=0, sticky="news", padx=20, pady=20)
        login_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=2)
        login_frame.grid_rowconfigure((1, 3), weight=1)
        login_frame.grid_columnconfigure((0, 1, 2), weight=1)

        login_title = tk.Label(
            login_frame, text="Login", bg="#F7F1EE", fg="#E7AEB2", font=("Arial", 16, "bold"))
        username_title = tk.Label(login_frame, text="Username",
                                  bg="#F7F1EE", fg="#4a4a4a", font=("Arial", 11, "bold"))
        username_entry = tk.Entry(login_frame, bg="white", borderwidth=0)
        password_title = tk.Label(login_frame, text="Password",
                                  bg="#F7F1EE", fg="#4a4a4a", font=("Arial", 11, "bold"))
        password_entry = tk.Entry(login_frame, bg="white", borderwidth=0)
        login_button = tk.Button(login_frame, text="Login", bg="#E7AEB2", fg="white", font=(
            "Arial", 11, "bold"), borderwidth=0, highlightthickness=0)

        login_title.grid(row=0, column=0, columnspan=3,
                         sticky="sew")
        username_title.grid(row=1, column=0, sticky="sw", padx=15)
        username_entry.grid(row=2, column=0, columnspan=3,
                            sticky="news", padx=15, pady=10)
        password_title.grid(row=3, column=0, sticky="sw", padx=15)
        password_entry.grid(row=4, column=0, columnspan=3,
                            sticky="news", padx=15, pady=10)
        login_button.grid(row=5, column=0, columnspan=3,
                          padx=15, pady=20, sticky="news")

    def setup_register_frame(self):
        register_frame = tk.Frame(self, bg="#F7F1EE")
        register_frame.grid(row=0, column=1, rowspan=3,
                            sticky="news", padx=20, pady=20)

        register_frame.grid_rowconfigure(
            (0, 2, 4, 6, 8, 10, 12), weight=2)
        register_frame.grid_rowconfigure(
            (1, 3, 5, 7, 9, 11), weight=1)
        register_frame.grid_columnconfigure((0, 1, 2), weight=1)

        register_title = tk.Label(
            register_frame, text="Register", bg="#F7F1EE", fg="#E7AEB2", font=("Arial", 16, "bold"))
        fullname_title = tk.Label(
            register_frame, text="Full Name", bg="#F7F1EE", fg="#4a4a4a", font=("Arial", 11, "bold"))
        fullname_entry = tk.Entry(register_frame, bg="white", borderwidth=0)
        username_title = tk.Label(
            register_frame, text="Username", bg="#F7F1EE", fg="#4a4a4a", font=("Arial", 11, "bold"))
        username_entry = tk.Entry(register_frame, bg="white", borderwidth=0)
        password_title = tk.Label(
            register_frame, text="Password", bg="#F7F1EE", fg="#4a4a4a", font=("Arial", 11, "bold"))
        password_entry = tk.Entry(register_frame, bg="white", borderwidth=0)
        email_title = tk.Label(
            register_frame, text="Email", bg="#F7F1EE", fg="#4a4a4a", font=("Arial", 11, "bold"))
        email_entry = tk.Entry(register_frame, bg="white", borderwidth=0)
        address_title = tk.Label(
            register_frame, text="Address", bg="#F7F1EE", fg="#4a4a4a", font=("Arial", 11, "bold"))
        address_entry = tk.Entry(register_frame, bg="white", borderwidth=0)

        register_button = tk.Button(
            register_frame, text="Register", bg="#E7AEB2", fg="white", font=("Arial", 11, "bold"), borderwidth=0, highlightthickness=0)

        register_title.grid(row=0, column=0, columnspan=3,
                            sticky="ew")
        fullname_title.grid(row=1, column=0, sticky="sw", padx=15)
        username_title.grid(row=3, column=0, sticky="sw", padx=15)
        password_title.grid(row=5, column=0, sticky="sw", padx=15)
        email_title.grid(row=7, column=0, sticky="sw", padx=15)
        address_title.grid(row=9, column=0, sticky="sw", padx=15)
        register_button.grid(row=12, column=0, columnspan=3,
                             padx=15, pady=30, sticky="news")

        fullname_entry.grid(row=2, column=0, columnspan=3,
                            sticky="news", padx=15, pady=5)
        username_entry.grid(row=4, column=0, columnspan=3,
                            sticky="news", padx=15, pady=5)
        password_entry.grid(row=6, column=0, columnspan=3,
                            sticky="news", padx=15, pady=5)
        email_entry.grid(row=8, column=0, columnspan=3,
                         sticky="news", padx=15, pady=5)
        address_entry.grid(row=10, column=0, columnspan=3,
                           sticky="news", padx=15, pady=5)
