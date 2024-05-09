import sqlite3
from data.Product import Product
from data.Order import Order
from data.Transaction import Transaction


class Database:
    def __init__(self) -> None:
        conn = sqlite3.connect("db/sqlite3_db.db")
        cursor = conn.cursor()
        self.conn, self.cursor = conn, cursor

    def get_transactions(self):
        sql = """
                SELECT transactions.transaction_id, transactions.user_id, transactions.transaction_status, transactions.payment_time, transactions.payment_amount, users.address
                FROM transactions
                JOIN users ON transactions.user_id = users.username;
                """
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        transactions = []
        for res in result:
            transaction_id, user_id, transaction_status, payment_time, payment_amount, address = res
            transaction = Transaction(transaction_id, user_id,
                                      transaction_status, payment_time, payment_amount, address)
            transactions.append(transaction)

        return transactions

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

    def insert_transaction(self, transaction: Transaction):

        sql = "INSERT INTO transactions (transaction_id, user_id, transaction_status, payment_time, payment_amount) VALUES (?, ?, ?, ?, ?)"

        # Tuple containing values for the SQL statement
        values = (transaction.transaction_id, transaction.user_id, transaction.transaction_status,
                  transaction.payment_time, transaction.payment_amount)

        # Execute the SQL statement
        self.cursor.execute(sql, values)
        self.conn.commit()

    def insert_order(self, order: Order):
        sql = "INSERT INTO orders (order_id, username, product_id, quantity) VALUES (?, ?, ?, ?)"
        values = (order.order_id, order.user.get_username(),
                  order.product.get_product_id(), order.quantity)
        self.cursor.execute(sql, values)
        self.conn.commit()
        

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
