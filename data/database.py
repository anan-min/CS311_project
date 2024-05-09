import sqlite3
from data.Product import Product


class Database:
    def __init__(self) -> None:
        conn = sqlite3.connect("db/sqlite3_db.db")
        cursor = conn.cursor()
        self.conn, self.cursor = conn, cursor

    def get_products(self):
        sql = "SELECT * FROM products"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        products = []
        for res in result:
            product_id, product_title, product_price, product_info, product_image = res
            product = Product(product_id, product_title,
                              product_price, product_info, product_image)
            products.append(product)

        return products

    def register_new_user(self, user_info):
        sql = "INSERT INTO users (username, fullname, password, email, address) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(sql, user_info)
        self.conn.commit()

    def is_correct_credential(self, username, password):
        sql = "SELECT * FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(sql, (username, password))
        result = self.cursor.fetchall()
        return True if result else False

    def get_user(self, username, password):
        sql = "SELECT * FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(sql, (username, password))
        return self.cursor.fetchone()

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


if __name__ == "__main__":
    db = Database()
    db.get_products()
