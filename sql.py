import pymysql as PyMySQL

# Connect to the database
host = 'localhost'
user = 'root'
password = 'qwerty@123'
db = 'Real_Database'

connection = PyMySQL.connect(host=host, user=user, password=password, db=db)

# Create a cursor object using the cursor() method
cursor = connection.cursor()

def Add_To_Realtor_Agency(Agency_Id , Agency_Owner , Star_Rating , Email , Phone):
    global cursor

    # SQL query string
    sql = "INSERT INTO Realtor_Agency (Agency_Id , Agency_Owner , Star_Rating , Email , Phone) VALUES (%s, %s, %s, %s, %s)"
    # Execute the sql query
    try:
        cursor.execute(sql, (Agency_Id , Agency_Owner , Star_Rating , Email , Phone))
        connection.commit()
    except PyMySQL.Error as e:
        print(e)
        return False
    return True

def Add_To_Realtor(Agency_Id , Employee_Id , Name , DateOfBirth , Contact_Info_Email , Contact_Info_Phone , S_Realtor_Id , Start_Date , Experience):
    global cursor
    # Error Checking for the input

    # SQL query string
    sql = "INSERT INTO Realtor (Agency_Id , Employee_Id , Name , DateOfBirth , Contact_Info_Email , Contact_Info_Phone , S_Realtor_Id , Start_Date , Experience) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # Execute the sql query
    try:
        cursor.execute(sql, (Agency_Id , Employee_Id , Name , DateOfBirth , Contact_Info_Email , Contact_Info_Phone , S_Realtor_Id , Start_Date , Experience))
        connection.commit()

    except PyMySQL.Error as e:
        print(e)
        return False
    return True

def View_Agency_Related_Properties(Agency_Id):
    global cursor
    sql = "SELECT * FROM Property as p JOIN Agencies_Employed as ae ON p.Owner_id = ae.Owner_ID AND ae.Agency_Id = %s"

    try:
        cursor.execute(sql, (Agency_Id))
        connection.commit()
        return cursor.fetchall()
    except PyMySQL.Error as e:
        print(e)
        return False
    return True

