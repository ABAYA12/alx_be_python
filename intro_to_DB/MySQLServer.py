#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host, user, and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database using uppercase SQL keywords
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    create_database()

