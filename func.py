"""
client functions
"""
import pymysql.cursors
import os
import datetime
from typing import Dict, Any, List, Tuple
import pymysql

def create_cursor():
    connection = pymysql.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection.cursor()