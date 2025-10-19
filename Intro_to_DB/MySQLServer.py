import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (replace user and password if different)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
