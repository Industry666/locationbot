from tools.appandDB_config import DB_CONFIG
import psycopg2


class ConnDB:
    @staticmethod
    def get_connect():
        conn = DB_CONFIG
        return conn

    @staticmethod
    def init_db(conn, force: bool = False):
        c = conn.cursor()

        if force:
            c.execute('DROP TABLE IF EXISTS user_message')
        c.execute('''CREATE TABLE IF NOT EXISTS user_message (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        location_name TEXT NOT NULL
        )
        ''')

        conn.commit()

    @staticmethod
    def add_message(conn, user_id: int, location_name: str):
        c = conn.cursor()
        c.execute(f"INSERT INTO user_message (user_id, location_name) "
                  f"VALUES ('{user_id}', '{location_name}')")
        conn.commit()

    @staticmethod
    def get_list_location(conn, user_id: int, limit=10):
        c = conn.cursor()
        c.execute(f"SELECT location_name FROM user_message "
                  f"WHERE user_id = '{user_id}' ORDER BY id DESC LIMIT '{limit}'")
        result = c.fetchall()
        return result

    @staticmethod
    def remove_all_locations(conn, user_id: int):
        c = conn.cursor()
        c.execute(f"DELETE FROM user_message WHERE user_id = '{user_id}'")
        conn.commit()
