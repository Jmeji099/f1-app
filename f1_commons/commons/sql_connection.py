import mysql.connector
from mysql.connector import Error

def get_info(conn):
    return conn.get_server_info()

def create_server_connection():
    '''
    Creates a connection to the database using the config above
    returns None if connection cannot be established
    '''
    conn = None
    try:
        conn = mysql.connector.connect(
            user='root',
            password='backendservice',
            host='localhost',
            database='f1App')
        print("MySQL Database connection Successful")

    except Error as e:
        print(f"Error: '{e}'")

    return conn


def read_query(conn, query):
    '''
    When Selecting data will return queried data to user
    May return None if no data is found
    '''
    cursor = conn.cursor()
    results = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: '{e}'")


def execute_query(conn, query):
    '''
    Simple query that does not need additional data
    '''
    cursor.conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Success")
    except Error as e:
        print(f"Error: '{e}'")


def execute_query(conn, sql, dataobject):
    '''
    Runs single sql command on multiple data "object"
    passed as a list
    '''
    cursor.conn.cursor()
    try:
        cursor.executemany(sql, val)
        conn.commit()
        print("Success")
    except Error as e:
        print(f"Error: '{e}'")


def close_connection(conn):
    '''
    closes the open connection and return none
    '''
    try:
        conn.close()
    except Exception as e:
        print(e)

    return None