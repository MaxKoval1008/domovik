import sqlite3


class UsersBase:

    def __init__(self, database) -> object:
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()

    def create_table_users(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
                         user_id INTEGER PRIMARY KEY, 
                         user_tel TEXT)''')

    def exists_user(self, user_id):
        return bool(self.cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone())

    def telephone_user(self, user_id):
        return self.cur.execute("SELECT user_tel FROM users WHERE user_id=?", (user_id,)).fetchone()

    def profile_user(self, user_id):
        return self.cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()

    def add_to_db_users(self, user_id, user_tel):
        self.cur.execute("INSERT INTO users(user_id, user_tel) VALUES(?,?)", (user_id, user_tel))
        self.conn.commit()

    def get_all_users(self):
        self.cur.execute("SELECT * FROM users")
        return self.cur.fetchall()

    def create_table_help(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS help(
                         help TEXT,
                         telephone TEXT,
                         FOREIGN KEY (telephone) REFERENCES users (user_tel))''')

    def add_application_help(self, text, user_tel):
        self.cur.execute("INSERT INTO help(help, telephone) VALUES(?,?)", (text, user_tel))
        self.conn.commit()

    def create_table_helpers(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS helper(
                         skills TEXT,
                         telephone TEXT, 
                         FOREIGN KEY (telephone) REFERENCES users (user_tel))''')

    def add_application_helper(self, text, user_tel):
        self.cur.execute("INSERT INTO helper(skills, telephone) VALUES(?,?)", (text, user_tel))
        self.conn.commit()

    def get_all_help(self):
        self.cur.execute("SELECT * FROM help")
        return self.cur.fetchall()

    def get_all_helper(self):
        self.cur.execute("SELECT * FROM helper")
        return self.cur.fetchall()