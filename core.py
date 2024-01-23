import mysql.connector


class Core:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="<mysql>",
            database="book_store_db"
        )

        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL,
            name VARCHAR(32) NOT NULL,
            email VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(32) NOT NULL,
            created_at TIMESTAMP
            )
            """
        )
        cursor.close()

    def insert_data(self, name, email, password):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"""
                INSERT INTO users (name, email, password, created_at)
                VALUES ("{name}", "{email}", "{password}", CURRENT_TIMESTAMP())
                """
            )
        except Exception as err:
            print(err)
            return False
        self.connection.commit()

    def get_users(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT * FROM users 
        """)
        data = cursor.fetchall()
        return data

    def check_email(self, email):
        cursor = self.connection.cursor()
        cursor.execute(f"""
        SELECT email, password FROM users WHERE email = '{email}'
        """)
        data = cursor.fetchall()
        return data
