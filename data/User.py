class User:
    def __init__(self, username, fullname, password, email, address):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.address = address

    @classmethod
    def from_userinfo(cls, userinfo):
        return cls(*userinfo)

    def get_fullname(self):
        return self.fullname

    def set_fullname(self, fullname):
        self.fullname = fullname

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def __str__(self):
        return f"User(fullname={self.fullname}, username={self.username}, email={self.email}, address={self.address})"
