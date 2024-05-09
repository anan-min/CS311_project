
import tkinter as tk
from tkinter import messagebox
from data.database import Database
from data.app_data import App_data
from data.User import User



class Auth_page(tk.Frame):
    LABEL_STYLE = {"bg": "#E7AEB2", "fg": "white",
                   "font": ("Arial", 12, "bold")}

    def __init__(self, app_data: App_data):
        content_area = app_data.get_content_area()
        super().__init__(content_area, bg="white")
        self.app_data = app_data
        self.config_auth_page()

    def config_auth_page(self):
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.setup_login_frame()
        self.setup_register_frame()
        self.attach_frame_to_parent()

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
            "Arial", 11, "bold"), borderwidth=0, highlightthickness=0, command=self.login_button_clicked)

        login_title.grid(row=0, column=0, columnspan=3,
                         sticky="sew")
        username_title.grid(row=1, column=0, sticky="sw", padx=15)
        username_entry.grid(row=2, column=0, columnspan=3,
                            sticky="news", padx=15, pady=10, ipadx=10, ipady=5)
        password_title.grid(row=3, column=0, sticky="sw", padx=15)
        password_entry.grid(row=4, column=0, columnspan=3,
                            sticky="news", padx=15, pady=10, ipadx=10, ipady=5)
        login_button.grid(row=5, column=0, columnspan=3,
                          padx=15, pady=20, sticky="news")

        self.login_entry = username_entry, password_entry

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
            register_frame, text="Register", bg="#E7AEB2", fg="white", font=("Arial", 11, "bold"), borderwidth=0, command=self.register_button_clicked)

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

        self.register_entry = username_entry, fullname_entry, password_entry, email_entry, address_entry

    def login_button_clicked(self):
        database = self.app_data.get_database()

        username_entry, password_entry = self.login_entry
        username_input, password_input = username_entry.get(
        ).strip(), password_entry.get().strip()

        # if not user and not pwd:
        if not username_input or not password_input:
            messagebox.showwarning(
                "Admin : ", "Username and password can't be empty")
            username_entry.focus_force()
        else:
            if database.is_correct_credential(username_input, password_input):
                self.login_user(username_input, password_input)
                messagebox.showwarning(
                    "Admin : ", "Login successfully")
            else:
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                messagebox.showwarning(
                    "Admin : ", "Incorrect Username or Password")

    def register_button_clicked(self):
        username_entry, fullname_entry, password_entry, email_entry, address_entry = self.register_entry

        username_input, fullname_input, password_input, email_input, address_input = fullname_entry.get(
        ), username_entry.get(), password_entry.get(), email_entry.get(), address_entry.get()

        user_info = username_input, fullname_input, password_input, email_input, address_input

        if not self.is_regis_form_filled():
            self.focus_unfilled_entry()
            messagebox.showwarning(
                "Admin : ", "All form need to be filled")
        else:
            if self.is_username_already_exist(username_input):
                username_entry.delete(0, tk.END)
                username_entry.focus_force()
                messagebox.showwarning(
                    "Admin : ", "username is already used")
            else:
                if self.is_email_already_used(email_input):
                    email_entry.delete(0, tk.END)
                    email_entry.focus_force()
                    messagebox.showwarning(
                        "Admin : ", "email is already used")
                else:
                    # register
                    self.register_new_user(user_info)
                    messagebox.showwarning(
                        "Admin : ", "User Register successfully")

            # check email
    def login_user(self, username, password):
        user_info = self.app_data.database.get_user(username, password)
        self.app_data.set_current_user(User(user_info))

    def register_new_user(self, user_info):
        database = self.app_data.get_database()
        self.app_data.set_current_user(User(user_info))

        return database.register_new_user(user_info)

    def is_username_already_exist(self, username):
        database = self.app_data.get_database()
        return database.is_username_already_exists(username)

    def is_email_already_used(self, email):
        database = self.app_data.get_database()
        return database.is_email_already_used(email)

    def is_regis_form_filled(self):
        return all(entry.get() for entry in self.register_entry)

    def focus_unfilled_entry(self):
        for entry in self.register_entry:
            if not entry.get():
                entry.focus_force()
                break

    def attach_frame_to_parent(self):
        self.app_data.switch_main_frame(self)
