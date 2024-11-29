"""
client functions
"""
import pymysql.cursors
import os
import datetime
from typing import Dict, Any, List, Tuple
import pymysql

# Global cursor
def create_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Leovaldez@1938',
        database='REAL_ESTATE',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def create_cursor(connection):
    return connection.cursor()

connection = create_connection()
cursor = create_cursor(connection)

def View_Agency_Related_Properties(agency_id):
    print("Hello")

def add_client(client_id , client_name , client_DOB , client_email , client_phone):
    add_query = "INSERT INTO Client VALUES (%s , %s , %s , %s , %s)"
    try :
        cursor.execute(add_query , (client_id , client_name , client_DOB , client_email , client_phone))
        connection.commit()
    except:
        print("Error in adding client")

def add_client_dependent(client_id , dependent_name , dependent_DOB , dependent_phone , dependent_email):
    add_query = "INSERT INTO Client_dependent VALUES (%s , %s , %s , %s , %s)"
    try :
        cursor.execute(add_query , (client_id , dependent_name , dependent_DOB , dependent_email , dependent_phone))
        connection.commit()
    except:
        print("Error in adding client dependent")

def add_client_to_ageny(client_id , agency_id):
    add_query = "INSERT INTO Client_agency VALUES (%s , %s)"
    try :
        cursor.execute(add_query , (client_id , agency_id))
        connection.commit()
    except:
        print("Error in adding client to agency")

def view_dep(client_id):
    view_query = "SELECT * FROM Client_dependent WHERE client_id = %s"
    try:
        cursor.execute(view_query , (client_id))
        result = cursor.fetchall()
        for row in result:
            print(row)
    except:
        print("Error in viewing dependent")

def view_agencies(client_id):
    view_query1 = "SELECT Agency_id FROM Agencies_Contacted WHERE client_id = %s"
    view_query2 = "SELECT * FROM Realtor_Agency WHERE agency_id = %s"
    try:
        cursor.execute(view_query1 , (client_id))
        result = cursor.fetchall()
        for row in result:
            cursor.execute(view_query2 , (row['Agency_id']))
            result2 = cursor.fetchall()
            for row2 in result2:
                print(row2)
    except:
        print("Error in viewing agencies")

def view_properties(client_id):
    view_query1 = "SELECT Agency_ID FROM Agencies_Contacted WHERE client_id = %s"
    try:
        cursor.execute(view_query1 , (client_id))
        result = cursor.fetchall()
        for row in result:
            View_Agency_Related_Properties(row['Agency_ID'])
    except:
        print("Error in viewing properties")

if __name__ == "__main__":
    view_agencies(1)