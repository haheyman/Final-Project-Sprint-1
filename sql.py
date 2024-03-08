import mysql.connector
from mysql.connector import Error

# Function to create database connection
def create_connection(hostname, userid, pswd, bdname):
    conn = None
    try:
        conn=mysql.connector.connect(
            host = hostname,
            user = userid,
            password = pswd,
            database = bdname
        )
        print("DB created successfully")
    except Error as e:
        print("Error is",e)
    return conn

#This function is a generic read function to get data from DB
def execute_read_query(myconnection, sql):
    rows = None
    cursor = myconnection.cursor(dictionary=True)
    try:

        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print('Error is',e)
        
