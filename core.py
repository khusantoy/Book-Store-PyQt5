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
        email VARCHAR(50) NOT NULL,
        password VARCHAR(15) NOT NULL 
        )
        """
    )
    cursor.close()

    def insert_data(self, ):