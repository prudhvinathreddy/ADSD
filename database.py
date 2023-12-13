import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create flowers table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS flowers (
                flower_id INTEGER PRIMARY KEY AUTOINCREMENT,
                flower_name TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')

        # Create colors table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS colors (
                color_id INTEGER PRIMARY KEY AUTOINCREMENT,
                color_name TEXT NOT NULL,
                flower_id INTEGER,
                FOREIGN KEY (flower_id) REFERENCES flowers(flower_id)
            )
        ''')

        self.conn.commit()

    def execute_query(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()
