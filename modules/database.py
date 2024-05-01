import sqlite3


class Database:
    def __init__(self) -> None:
        conn = sqlite3.connect("database/login.db")
        cursor = conn.cursor()
        self.conn, self.cursor = conn, cursor

    def is_username_exists(self, username):
        sql = f"select * from student where username='{username}';"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return True if result else False

    def get_user_from_cred(self, username, password):
        sql = "select * from student where username=? and password=?;"
        self.cursor.execute(sql, [username, password])
        result = self.cursor.fetchone()

        return result

    def is_corrrect_credentials(self, username, password):
        sql = "select * from student where username=? and password=?;"
        self.cursor.execute(sql, [username, password])
        result = self.cursor.fetchall()

        return True if result else False

    def is_course_already_exists(self, course_code, course_name):
        sql = f"SELECT * FROM course WHERE course_code = '{course_code}' OR course_name = '{course_name}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        return True if result else False

    def is_course_code_exists(self, course_code):
        sql = f"SELECT * FROM course where course_code = '{course_code}';"
        # execute step
        self.cursor.execute(sql)
        # fetch result
        result = self.cursor.fetchone()

        return True if result else False

    def is_course_name_exists(self, course_name):
        sql = f"SELECT * FROM course WHERE course_name='{course_name}'"
        # execute step
        self.cursor.execute(sql)
        # fetch result
        result = self.cursor.fetchone()
        return True if result else False

    def insert_new_course(self, course_code, course_name, day, roombox):
        sql = f"INSERT INTO course (course_code, course_name, day, room ) values ('{course_code}', '{course_name}', '{day}', '{roombox}') "
        self.cursor.execute(sql)
        self.conn.commit()

    def update_course(self, day, room, course_code):
        sql = f"UPDATE course SET day = '{day}', room = '{room}' WHERE course_code = '{course_code}'"
        self.cursor.execute(sql)
        self.conn.commit()

    def update_course(self, course_name, day, room, course_code):
        sql = f"UPDATE course SET course_name = '{course_name}', day = '{day}', room = '{room}' WHERE course_code = '{course_code}'"

        self.cursor.execute(sql)
        self.conn.commit()

    def get_courses(self):
        sql = "select * from course;"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def delete_course(self, course_id):
        sql = f"DELETE FROM course WHERE id='{course_id}'"
        self.cursor.execute(sql)
        self.conn.commit()


    def close_connection(self):
        self.cursor.close()
        self.conn.close()
