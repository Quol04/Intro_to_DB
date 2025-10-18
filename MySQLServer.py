#!/usr/bin/python3
"""
A script to create a MySQL database named 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='770479'  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: confirm closing
            # print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
