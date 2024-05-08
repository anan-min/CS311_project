import sqlite3


class Database:
    def __init__(self) -> None:
        conn = sqlite3.connect("db/sqlite3_db.db")
        cursor = conn.cursor()
        self.conn, self.cursor = conn, cursor

    def register_new_user(self, user_info):
        sql = "INSERT INTO users (username, fullname, password, email, address) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(sql, user_info)
        self.conn.commit()

    def is_correct_credential(self, username, password):
        sql = "SELECT * FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(sql, (username, password))
        result = self.cursor.fetchall()
        return True if result else False

    def is_username_already_exists(self, username):
        sql = "SELECT * FROM users WHERE username = ?"
        self.cursor.execute(sql, (username, ))
        result = self.cursor.fetchall()
        return True if result else False

    def is_email_already_used(self, email):
        sql = "SELECT * FROM users WHERE email = ?"
        self.cursor.execute(sql, (email, ))
        result = self.cursor.fetchall()
        return True if result else False

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
