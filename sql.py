import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host, username, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            passwd=password,
        )
        print("MySQL Database connection successfully.")
    except Error as e:
        print(f'Error: {e}')
    
    return connection

def create_db_connection(host, username, password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            passwd=password,
            database = db_name
        )
        print("MySQL Database connection successfully.")
    except Error as e:
        print(f'Error: {e}')
    
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f'Error: {e}')

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        cursor.commit()
        print("Query")
    except Error as e:
        print(f'Error: {e}')

user = "root"
pw = "juGG3rn@ut"
db = "osu"

connection = create_server_connection("localhost", user, pw)
create_database_query = "CREATE DATABASE osu"
create_database(connection, create_database_query)
connection = create_server_connection("localhost", user, pw, db)