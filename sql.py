import pymysql

# Connect to the database
host = 'localhost'
user = 'root'
password = 'qwerty@123'
db = 'Real_Database'

connection = pymysql.connect(host=host, user=user, password=password, db=db)

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
    except pymysql.Error as e:
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

    except pymysql.Error as e:
        print(e)
        return False
    return True

def View_Agency_Related_Properties(Agency_Id):
    global cursor
    sql = "SELECT * FROM Property as p JOIN Agencies_Employed as ae ON p.Owner_id = ae.Owner_ID AND ae.Agency_Id = %s"

    try:
        cursor.execute(sql, (Agency_Id))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(row)
    except pymysql.Error as e:
        print(e)
        return False
    return True

def View_Agency_Related_Clients(Agency_Id):
    global cursor
    sql = "SELECT c.Client_Id as ID, c.Name as Name , c.DateOfBirth as DOB , c.Contact_Info_Email as Email , c.Contact_Info_Phone as Phone FROM Client as c JOIN Agencies_Contacted as ac ON c.Client_ID = ac.Client_ID AND ac.Agency_Id = %s"

    try:
        cursor.execute(sql, (Agency_Id))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(row)
            print("\n")
            view_dep(row[0])
    except pymysql.Error as e:
        print(e)
        return False
    return True

def View_Agency_Related_Owners(Agency_Id):
    global cursor
    sql = "SELECT o.Owner_id Owner_Id, o.Name Name, o.DOB DOB, o.Owner_Type Type FROM Owner as o JOIN Agencies_Employies as ae ON o.Owner_id = ae.Owner_ID AND ae.Agency_ID = %s"

    try:
        cursor.execute(sql, (Agency_Id))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(row)   
    except pymysql.Error as e:
        print(e)
        return False
    return True

def View_Agency_Related_Realtors(Agency_Id):
    global cursor
    sql = "SELECT r.Employee_Id Employee_Id, r.Name Name, r.DateOfBirth DOB, r.Contact_Info_Email Email, r.Contact_Info_Phone Phone, r.S_Realtor_Id Supervisor_Id, r.Start_Date Start_Date, r.Experience Experience FROM Realtor as r WHERE r.Agency_Id = %s"

    try:
        cursor.execute(sql, (Agency_Id))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(row)
    except pymysql.Error as e:
        print(e)
        return False
    return True

def View_Agency_Related_Realtors_With_Experience(Agency_Id , Experience):
    global cursor
    sql = "SELECT r.Employee_Id Employee_Id, r.Name Name, r.DateOfBirth DOB, r.Contact_Info_Email Email, r.Contact_Info_Phone Phone, r.S_Realtor_Id Supervisor_Id, r.Start_Date Start_Date, r.Experience Experience FROM Realtor as r WHERE r.Agency_Id = %s AND r.Experience > %s"

    try:
        cursor.execute(sql, (Agency_Id))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(row)
    except pymysql.Error as e:
        print(e)
        return False
    return True

def Update_Client(Client_Id , Name , DateOfBirth , Contact_Info_Email , Contact_Info_Phone):
    global cursor
    sql = "UPDATE Client SET Name = %s, DateOfBirth = %s, Contact_Info_Email = %s, Contact_Info_Phone = %s WHERE Client_Id = %s"
    try:
        cursor.execute(sql, (Name , DateOfBirth , Contact_Info_Email , Contact_Info_Phone , Client_Id))
        connection.commit()
    except PyMySQL.Error as e:
        print(e)
        return False
    return True


def Best_Realtor(Agency_Id):
    global cursor
    sql = "SELECT r.Employee_Id Employee_Id, r.Name Name, r.DateOfBirth DOB, r.Contact_Info_Email Email, r.Contact_Info_Phone Phone, r.S_Realtor_Id Supervisor_Id, r.Start_Date Start_Date, r.Experience Experience FROM Realtor as r WHERE r.Agency_Id = %s and Experience = (SELECT MAX(Experience) FROM Realtor WHERE Agency_Id = %s)"

    try:
        cursor.execute(sql, (Agency_Id , Agency_Id))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(row)
    except PyMySQL.Error as e:
        print(e)
        return False
    return True

def Area_Under_Venture(License , PID , VID):
    global cursor
    sql = "SELECT SUM(Area) FROM Property JOIN Properties_Included as pi ON Property.PID = pi.PID WHERE pi.License = %s AND pi.VID = %s"

    try:
        cursor.execute(sql, (License , VID))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(row)
    except PyMySQL.Error as e:
        print(e)
        return False
    return True


