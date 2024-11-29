
import pymysql
import datetime
# Global variable for the cursor
cursor = None
connection = None

def connect_mysql():
    global cursor
    global connection
    try:
        # Establish the connection
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='Leovaldez@1938',
            database='REAL_ESTATE'
        )

        print("Successfully connected to the database")

        # Create a cursor object
        cursor = connection.cursor()

    except pymysql.MySQLError as e:
        print(f"Error: {e}")


"""Client Part"""



def add_client(client_id , client_name , client_DOB , client_email , client_phone):
    global cursor
    add_query = "INSERT INTO Client VALUES (%s , %s , %s , %s , %s)"
    try :
        cursor.execute(add_query , (client_id , client_name , client_DOB , client_email , client_phone))
        connection.commit()
    except:
        print("Error in adding client")

def add_client_dependent(client_id , dependent_name , dependent_DOB , dependent_email , dependent_phone):
    global cursor
    add_query = "INSERT INTO Client_Dependent VALUES (%s , %s , %s , %s , %s)"
    try :
        cursor.execute(add_query , (client_id , dependent_name , dependent_DOB , dependent_email , dependent_phone))
        connection.commit()
    except pymysql.Error as e:
        print(e)
        return False
    return True

def add_client_to_agency(client_id , agency_id):
    global cursor
    add_query = "INSERT INTO Agencies_Contacted VALUES (%s , %s)"
    try :
        cursor.execute(add_query , (client_id , agency_id))
        connection.commit()
    except pymysql.Error as e:
        print(e)
        return False
    return True

def view_dep(client_id,to_print):
    global cursor
    view_query = "SELECT * FROM Client_Dependent WHERE client_id = %s"
    try:
        cursor.execute(view_query , (client_id))
        result = cursor.fetchall()
        if(cursor != None and to_print == 1):
            print("Dependents of client with ID:",client_id)
        for row in result:
            print(tuple(map(str, row)))
    except pymysql.Error as e:
        print(e)
        return False
    return True

def view_agencies(client_id):
    global cursor
    view_query1 = "SELECT Agency_id FROM Agencies_Contacted WHERE client_id = %s"
    view_query2 = "SELECT * FROM Realtor_Agency WHERE agency_id = %s"
    try:
        cursor.execute(view_query1 , (client_id))
        result = cursor.fetchall()
        for row in result:
            cursor.execute(view_query2 , (row[0]))
            result2 = cursor.fetchall()
            for row2 in result2:
                print(tuple(map(str, row2)))
    except pymysql.Error as e:
        print(e)
        return False
    return True

def view_properties(client_id):
    global cursor
    view_query1 = "SELECT Agency_ID FROM Agencies_Contacted WHERE client_id = %s"
    try:
        cursor.execute(view_query1 , (client_id))
        result = cursor.fetchall()
        for row in result:
            View_Agency_Related_Properties(row[0])
    except pymysql.Error as e:
        print(e)
        return False
    return True
"""Realtor_agency Part"""

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
    if(S_Realtor_Id == ""):
        S_Realtor_Id = None
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
            print(tuple(map(str, row)))
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
            print("Client is:")
            print(tuple(map(str, row)))
            print("\n")
            view_dep(row[0],1)
            print("\n")
    except pymysql.Error as e:
        print(e)
        return False
    return True

def View_Agency_Related_Owners(Agency_Id):
    global cursor
    sql = "SELECT o.Owner_id Owner_Id, o.Name Name, o.DOB DOB, o.Owner_Type Type FROM Owner as o JOIN Agencies_Employed as ae ON o.Owner_id = ae.Owner_ID AND ae.Agency_ID = %s"

    try:
        cursor.execute(sql, (Agency_Id))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(tuple(map(str, row)))   
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
            print(tuple(map(str, row)))
    except pymysql.Error as e:
        print(e)
        return False
    return True

def View_Agency_Related_Realtors_With_Experience(Agency_Id , Experience):
    global cursor
    sql = "SELECT r.Employee_Id Employee_Id, r.Name Name, r.DateOfBirth DOB, r.Contact_Info_Email Email, r.Contact_Info_Phone Phone, r.S_Realtor_Id Supervisor_Id, r.Start_Date Start_Date, r.Experience Experience FROM Realtor as r WHERE r.Agency_Id = %s AND r.Experience > %s"

    try:
        cursor.execute(sql, (Agency_Id,Experience))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(tuple(map(str, row)))
    except pymysql.Error as e:
        print(e)
        return False
    return True

"""Developer and Govt part"""
def add_developer(
    license_no, name, expiry_date, no_of_projects,
    revenue_first, revenue_second, revenue_third, revenue_fourth, revenue_fifth
):
    global cursor
    try:
        license_no = None if license_no == "" else license_no
        name = None if name == "" else name
        expiry_date = None if expiry_date == "" else expiry_date
        no_of_projects = None if no_of_projects == "" else no_of_projects
        revenue_first = None if revenue_first == "" else revenue_first
        revenue_second = None if revenue_second == "" else revenue_second
        revenue_third = None if revenue_third == "" else revenue_third
        revenue_fourth = None if revenue_fourth == "" else revenue_fourth
        revenue_fifth = None if revenue_fifth == "" else revenue_fifth
        # SQL query to insert a new developer
        query = """
            INSERT INTO Developer (
                License, Name, Expiry_Date, No_of_projects,
                Revenue_first_project, Revenue_second_project,
                Revenue_third_project, Revenue_fourth_project,
                Revenue_fifth_project
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # Execute the query with provided values
        cursor.execute(query, (
            license_no, name, expiry_date, no_of_projects,
            revenue_first, revenue_second, revenue_third,
            revenue_fourth, revenue_fifth
        ))
        
        connection.commit()
        
        print(f"Developer '{name}' added successfully.")
    except Exception as e:
        print("Error while adding developer:", e)



# Function to add multiple entries to the Favourable_Crops table
def add_favourable_crops(property_ids, crop_names):
    global cursor
    try:
        query = """
            INSERT INTO Favourable_Crops (Property_id, Crop_Name)
            VALUES (%s, %s)
        """
        # Loop through the inputs and execute the query for each pair
        for property_id, crop_name in zip(property_ids, crop_names):
            cursor.execute(query, (property_id, crop_name))
        
        connection.commit()
        print("Favourable crops added successfully.")
    except Exception as e:
        print("Error adding favourable crops:", e)


# Function to add multiple entries to the Nearby_Water_Sources table
def add_nearby_water_sources(property_ids, water_sources):
    global cursor
    try:
        query = """
            INSERT INTO Nearby_Water_Sources (Property_id, Water_Sources)
            VALUES (%s, %s)
        """
        # Loop through the inputs and execute the query for each pair
        for property_id, water_source in zip(property_ids, water_sources):
            cursor.execute(query, (property_id, water_source))
        
        connection.commit()
        print("Nearby water sources added successfully.")
    except Exception as e:
        print("Error adding nearby water sources:", e)


# Function to add to Residential table
def add_residential(property_id, name, property_type):
    global cursor
    try:
        query = """
            INSERT INTO Residential (Property_id, Name, Type)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (property_id, name, property_type))
        
        connection.commit()
        print("Residential property added successfully.")
    except Exception as e:
        print("Error adding residential property:", e)

# Function to add to Industrial table
def add_industrial(property_id, name):
    global cursor
    try:
        query = """
            INSERT INTO Industrial (Property_id, Name)
            VALUES (%s, %s)
        """
        cursor.execute(query, (property_id, name))
        
        connection.commit()
        print("Industrial property added successfully.")
    except Exception as e:
        print("Error adding industrial property:", e)

# Function to add to Commercial table
def add_commercial(property_id, name, property_type):
    global cursor
    try:
        query = """
            INSERT INTO Commercial (Property_id, Name, Type)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (property_id, name, property_type))
        
        connection.commit()
        print("Commercial property added successfully.")
    except Exception as e:
        print("Error adding commercial property:", e)

# Function to add to Agricultural table
def add_agricultural(property_id, soil_type):
    global cursor
    try:
        query = """
            INSERT INTO Agricultural (Property_id, Soil_Type)
            VALUES (%s, %s)
        """
        cursor.execute(query, (property_id, soil_type))
        
        connection.commit()
        print("Agricultural property added successfully.")
    except Exception as e:
        print("Error adding agricultural property:", e)

def add_owner(
    owner_id, name, dob, owner_type
):
    global cursor
    try:
        # If owner_id is empty, set it to 1
        owner_id = 1 if owner_id == "" else owner_id
        
        # Replace empty strings with None (which translates to NULL in SQL)
        # name = None if name == "" else name
        # dob = None if dob == "" else dob
        # owner_type = None if owner_type == "" else owner_type

        # SQL query to insert a new owner
        query = """
            INSERT INTO Owner (
                Owner_id, Name, DOB, Owner_type
            ) VALUES (%s, %s, %s, %s)
        """
        # Execute the query with the updated values
        cursor.execute(query, (
            owner_id, name, dob, owner_type
        ))
        
        # Commit the transaction
        connection.commit()
        print(f"Owner with ID '{owner_id}' added successfully.")
    except Exception as e:
        print("Error while adding owner:", e)

def add_property(
    property_id, location_latitude, location_longitude, area, owner_id
):
    global cursor
    try:
        # If owner_id is empty, set it to 1
        # owner_id = 1 if owner_id == "" else owner_id
        
        # Replace empty strings with None (which translates to NULL in SQL)
        # location_latitude = None if location_latitude == "" else location_latitude
        # location_longitude = None if location_longitude == "" else location_longitude
        # area = None if area == "" else area

        # SQL query to insert a new property
        query = """
            INSERT INTO Property (
                Property_id, Location_Latitude, Location_Longitude, Area, Owner_id
            ) VALUES (%s, %s, %s, %s, %s)
        """
        # Execute the query with the updated values
        cursor.execute(query, (
            property_id, location_latitude, location_longitude, area, owner_id
        ))
        
        connection.commit()
        print(f"Property with ID '{property_id}' added successfully.")
    except Exception as e:  
        print("Error while adding property:", e)

def add_venture_and_property_included(
    vid, pid, license, owner_id, land_usage, 
    owner_equity, developer_equity, agreed_budget, property_id
):
    global cursor
    try:
        # Handle empty strings and set NULL for SQL
        # license = None if license == "" else license
        # owner_id = 1 if owner_id == "" else owner_id  # Default to 1 if empty
        # land_usage = None if land_usage == "" else land_usage
        # owner_equity = None if owner_equity == "" else owner_equity
        # developer_equity = None if developer_equity == "" else developer_equity
        # agreed_budget = None if agreed_budget == "" else agreed_budget
        property_id = None if property_id == "" else property_id
        
        # Insert into Venture table
        venture_query = """
            INSERT INTO Venture (
                VID, PID, License, Owner_id, Land_Usage,
                Monetary_Terms_Owner_Equity, Monetary_Terms_Developer_Equity,
                Monetary_Terms_Agreed_Budget
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(venture_query, (
            vid, pid, license, owner_id, land_usage, 
            owner_equity, developer_equity, agreed_budget
        ))

        # Insert into properties_included table
        properties_included_query = """
            INSERT INTO Properties_included (vid, license, pid, owner_id, property_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(properties_included_query, (
            vid, license, pid, owner_id, property_id
        ))

        # Commit the transaction
        connection.commit()
        print(f"Venture with ID '{vid}' and Property with ID '{property_id}' added successfully.")
    except Exception as e:
        print("Error while adding venture and linking to property:", e)

def get_all_project_venture_details():
    global cursor
    try:
        # SQL query to join Project, Venture, and properties_included tables
        query = """
            SELECT
                p.PID, 
                p.License AS Project_License, 
                p.Project_Name,
                p.Budget,
                p.Completion_Date,
                p.Revenue_incurred,
                v.Owner_id,
                v.Land_Usage,
                v.Monetary_Terms_Owner_Equity,
                v.Monetary_Terms_Developer_Equity,
                v.Monetary_Terms_Agreed_Budget,
                pi.property_id
            FROM Project p
            JOIN Venture v ON p.PID = v.PID
            JOIN properties_included pi ON v.PID = pi.pid;
        """
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Check if results exist
        if results:
            for row in results:
                print("PID:", row[0])
                print("Project License:", row[1])
                print("Project Name:", row[2])
                print("Budget:", row[3])
                print("Completion Date:", row[4])
                print("Revenue Incurred:", row[5])
                print("Owner ID:", row[6])
                print("Land Usage:", row[7])
                print("Monetary Terms Owner Equity:", row[8])
                print("Monetary Terms Developer Equity:", row[9])
                print("Monetary Terms Agreed Budget:", row[10])
                print("Property ID:", row[11])
                print("===============================================")
        else:
            print("No data found.")
    
    except Exception as e:
        print("Error while retrieving project and venture details:", e)

def add_project(pid,license,project_name,budget,completion_date,revenue_incurred):
    global cursor
    try:
        # Handle empty strings and set NULL for SQL
        # pid = 1 if pid == "" else pid  # Default to 1 if empty
        # license = None if license == "" else license
        # project_name = None if project_name == "" else project_name
        # budget = None if budget == "" else budget
        # completion_date = None if completion_date == "" else completion_date
        # revenue_incurred = None if revenue_incurred == "" else revenue_incurred
        
        # SQL query to insert a new project
        query = """
            INSERT INTO Project VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Execute the query with the updated values
        cursor.execute(query, (
            pid, license, project_name, budget, completion_date, revenue_incurred
        ))
        
        # Commit the transaction
        connection.commit()
        print(f"Project with ID '{pid}' added successfully.")
    except Exception as e:
        print("Error while adding project:", e)

def view_projects(license):
    query1 = "SELECT * FROM Project WHERE License = %s"
    try:
        cursor.execute(query1, (license))
        result = cursor.fetchall()
        for row in result:
            print(tuple(map(str, row)))
    except Exception as e:  
        print("Error while viewing projects:", e)

def view_ventures(pid , license):
    query = "SELECT * FROM Venture WHERE PID = %s AND License = %s"
    try:
        cursor.execute(query, (pid, license))
        result = cursor.fetchall()
        for row in result:
            print(tuple(map(str, row)))
    except Exception as e:
        print("Error while viewing ventures:", e)

def is_valid_phone_number(phone):
    # Check if the phone number is a string of length 10
    if len(phone) != 10:
        return False
    # Check if all characters are digits
    if not phone.isdigit():
        return False
    # Check if the first digit is not '0'
    if phone[0] == '0':
        return False
    return True


# update query
def Update_Client(Client_Id , Name , DateOfBirth , Contact_Info_Email , Contact_Info_Phone):
    global cursor
    sql = "UPDATE Client SET Name = %s, DateOfBirth = %s, Contact_Info_Email = %s, Contact_Info_Phone = %s WHERE Client_Id = %s"
    try:
        cursor.execute(sql, (Name , DateOfBirth , Contact_Info_Email , Contact_Info_Phone , Client_Id))
        connection.commit()
    except pymysql.Error as e:
        print(e)
        return False
    return True

# Aggregate query
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
    except pymysql.Error as e:
        print(e)
        return False
    return True

# Agrregate query
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
    except pymysql.Error as e:
        print(e)
        return False
    return True

# Delete query
def Delete_ClientDep(Client_Id , Dep_name):
    global cursor
    sql = "DELETE FROM Client_dependent WHERE Client_Id = %s AND Name = %s"
    try:
        cursor.execute(sql, (Client_Id , Dep_name))
        connection.commit()
    except pymysql.Error as e:
        print(e)
        return False
    
# Complex Query1 : # Give a code for this List those owners which have properties avergae land area > A
def Analysis_Query1(A):
    global cursor
    sql = """
    SELECT o.Owner_id, o.Name, AVG(p.Area) as Avg_Area
    FROM Owner o
    JOIN Property p ON o.Owner_id = p.Owner_id
    GROUP BY o.Owner_id, o.Name
    HAVING Avg_Area > %s
    """
    try:
        cursor.execute(sql, (A))
        connection.commit()
        # Print the result
        result = cursor.fetchall()
        for row in result:
            print(row)
    except pymysql.Error as e:
        print(e)
        return False
    return True

def Analysis_Query2(P , S):
    global cursor
    sql_query = "SELECT Name , License , AVG(Revenue_incurred) AS Avg_rev FROM (Developer JOIN Project ON Developer.License = Project.License)  GROUP BY License HAVING No_of_projects > %s AND Avg_rev > %s"
    try:
        cursor.execute(sql_query , (P , S))
        connection.commit()
        result = cursor.fetchall()
        for row in result:
             print(tuple(map(str, row)))
    except pymysql.Error as e:
        print(e)
        return False
    return True


def handle_client():
    while(1):
        print("What do you want to do?")
        print("1.Add Client.")
        print("2.Add dependents of a particular client.")
        print("3.Contact a particular agency for a particular client.")
        print("4.View dependents of a particular client.")
        print("5.View properties ready to buy for a client.")
        print("6. Exit")
        choice = int(input("Enter number which you want:"))
        if(choice == 1):
            client_id = input("Enter client id:(integer)")
            name = input("Enter name:")
            dob = input("Enter dob:(YYYY-MM-DD)")
            email = input("Enter email:")
            phone = input("Enter phone number: ")
            while not is_valid_phone_number(phone):
                print("Invalid phone number. Please enter a 10-digit number starting with a non-zero digit.")
                phone = input("Enter phone number: ")
            add_client(client_id,name,dob,email,phone)
        elif(choice == 2):
            no_clients = input("Enter number of dependents to add:")
            for i in range(int(no_clients)):
                client_id = input("Enter client id:(integer) for client who dependents to add:")
                name = input("Enter name for dependent to add:")
                dob = input("Enter dob(YYYY-MM-DD) of dependent to add:")
                email = input("Enter email of dependent to add:")
                phone = input("Enter phone number: ")
                while not is_valid_phone_number(phone):
                    print("Invalid phone number. Please enter a 10-digit number starting with a non-zero digit.")
                    phone = input("Enter phone number: ")
                add_client_dependent(client_id,name,dob,email,phone)
        elif (choice == 3):
            client_id = input("Enter client id:(integer) for client who want to contact agency:")
            agency_id = input("Enter agency id:(integer) of agency to contact:")
            add_client_to_agency(client_id,agency_id)
        elif (choice == 4):
            client_id = input("Enter client id:(integer) for client whose dependents to use:")
            view_dep(client_id,0)
        elif(choice == 5):
            client_id = input("Enter client whose properties to see:")
            view_properties(client_id)
        elif(choice == 6):
            break
        else:
            print("Invalid choice. Please try again.")

def handle_govt():
    while True:
        print("What do you want to do?")
        print("1. Add a property.")
        print("2. Add owner.")
        # print("View stuff lol")
        print("3. Exit")
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            property_id = input("Enter property ID (integer): ")
            location_longtitude = input("Enter location longtitude (decimal): ")
            location_latitude = input("Enter location latitude (decimal): ")
            area = input("Enter area (integer): ")
            owner_id = input("Enter owner ID (integer): ")
            add_property(property_id,location_longtitude,location_latitude,area,owner_id)
            type = input("Enter type of property (enter number):\nOptions are:1.Agricultural 2.Residential 3.Commercial 4.Industrial\n")
            if type == 1:
                soil_type = input("Enter soil type:")
                add_agricultural(property_id,soil_type)
                water_sources = input("Enter nearby water sources:").split()
                for i in water_sources:
                   add_nearby_water_sources(property_id,i)
                fav_crops = input("Enter favourable crops:").split()
                for i in fav_crops:
                    add_favourable_crops(property_id,i)
            elif type == 2:
                name = input("Enter name of residential property:")
                type = input("Enter type of residential property:")
                add_residential(property_id,name,type)
            elif type == 3:
                name = input("Enter name of commercial property:")
                type = input("Enter type of commercial property:")    
                add_commercial(property_id,name,type)
            elif type == 4:
                name = input("Enter name of industrial property:")
                add_industrial(property_id,name)
        
        elif choice == 2:
            owner_id = input("Enter owner ID (integer): ")
            name = input("Enter owner name: ")
            dob = input("Enter owner dob (YYYY-MM-DD): ")
            owner_type = input("Enter owner type: ")
            add_owner(owner_id,name,dob,owner_type)

        elif choice == 3:
            break
            
        else:
            print("Invalid choice. Please try again.")
        
        

def handle_developers():
    while True:
        print("What do you do?")
        print("1. Add a developer.")
        print("2. Add a project of a respective developer.")
        print("3. Add a venture of a respective project.")
        print("4. View projects associated with a particular developer.")
        print("5. View ventures related to a particular project.")
        print("6. Exit")
        choice = int(input("Enter the number of your choice: "))
        if(choice == 1):
            license = input("Enter license:")
            name = input("Enter name of developer:")
            expiry_date =input("Enter expiry date of license(YYYY-MM-DD):")
            no_projects = input("Enter number of projects:")
            revenue_first = ""
            revenue_second = ""
            revenue_third = ""
            revenue_fourth = ""
            revenue_fifth = ""
            project_no = int(no_projects)
            if(project_no>= 1):
                revenue_first = input("Enter revenue of first project:")
            if(project_no>= 2):
                revenue_second = input("Enter revenue of second project:")
            if(project_no>= 3):
                revenue_third = input("Enter revenue of third project:")
            if(project_no>= 4):
                revenue_fourth = input("Enter revenue of fourth project:")
            if(project_no>= 5):
                revenue_fifth = input("Enter revenue of fifth project:")
            add_developer(license,name,expiry_date,no_projects,revenue_first,revenue_second,revenue_third,revenue_fourth,revenue_fifth) 

        elif(choice == 2):
            pid = input("Enter Project ID (PID): ")
            license = input("Enter License (max 50 characters): ")
            project_name = input("Enter Project Name (max 100 characters): ")
            budget = input("Enter Budget (integer): ")
            completion_date = input("Enter Completion Date (YYYY-MM-DD): ")
            revenue_incurred = input("Enter Revenue Incurred (integer): ")
            add_project(pid,license,project_name,budget,completion_date,revenue_incurred)
        
        elif choice == 3:
            vid = input("Enter VID (integer): ")
            pid = input("Enter PID (integer): ")
            license = input("Enter License (max 50 characters): ")
            owner_id = input("Enter Owner ID (integer): ")
            land_usage = input("Enter Land Usage (integer): ")
            owner_equity = input("Enter Monetary Terms Owner Equity (decimal): ")
            developer_equity = input("Enter Monetary Terms Developer Equity (decimal): ")
            agreed_budget = input("Enter Monetary Terms Agreed Budget (decimal or leave blank for NULL): ")
            agreed_budget = input("Enter Monetary Terms Agreed Budget (decimal): ")
            property_id = input("Enter Property ID (integer)")
            add_venture_and_property_included(vid,pid,license,owner_id,land_usage,owner_equity,developer_equity,agreed_budget,property_id)
        
        elif choice == 4:
            license = input("Enter License of developer whose projects to view(max 50 characters): ")
            view_projects(license)
        
        elif choice == 5:
            pid = input("Enter PID of project whose ventures to view: ")
            license = input("Enter License of project whose ventures to view(max 50 characters): ")
            view_ventures(pid , license)
    
        elif choice == 6:
            break

        else:
            print("Invalid choice. Please try again.")

def handle_realtor_agency():
    while True: 
        print("What do you want to do?")
        print("1. Add a realtor agency.")
        print("2. Add a realtor.")
        print("3. View all properties of a particular agency.")
        print("4. View client and dependents associated with a particular agency.")
        print("5. View owners associated with a particular agency.")
        print("6. View realtors (with optional experience requirement).")
        print("7. Exit")
        choice = int(input("Enter the number of your choice: "))
        
        if choice == 1:
            agency_id = input("Enter agency ID (integer): ")
            agency_owner= input("Enter agency owner name: ")
            star_rating = input("Enter agency star rating (1-5): ")
            email = input("Enter agency email: ")
            phone = input("Enter phone number: ")
            while not is_valid_phone_number(phone):
                print("Invalid phone number. Please enter a 10-digit number starting with a non-zero digit.")
                phone = input("Enter phone number: ")
            Add_To_Realtor_Agency(agency_id,agency_owner,star_rating,email,phone)
        
        elif choice == 2:
            agency_id = input("Enter agency ID (integer) the realtor belongs to: ")
            realtor_id = input("Enter realtor ID (integer): ")
            name = input("Enter realtor name: ")
            dob = input("Enter realtor dob (YYYY-MM-DD): ")
            email = input("Enter realtor email: ")
            phone = input("Enter phone number: ")
            s_realtor_id = input("Enter supervisor realtor ID (integer) or leave blank if none: ")
            start_date = input("Enter realtor start date (YYYY-MM-DD): ")
            experience = input("Enter realtor experience (in years): ")
            while not is_valid_phone_number(phone):
                print("Invalid phone number. Please enter a 10-digit number starting with a non-zero digit.")
                phone = input("Enter phone number: ")
            Add_To_Realtor(agency_id,realtor_id,name,dob,email,phone,s_realtor_id,start_date,experience)
        
        elif choice == 3:
            agency_id = input("Enter agency ID (integer) to view properties: ")
            View_Agency_Related_Properties(agency_id)
        
        elif choice == 4:
            agency_id = input("Enter your agency ID (integer): ")
            View_Agency_Related_Clients(agency_id)
        
        elif choice == 5:
            agency_id = input("Enter your agency ID (integer): ")
            View_Agency_Related_Owners(agency_id)
        
        elif choice == 6:
            agency_id = input("Enter your agency ID (integer): ")
            experience = input("Enter minimum experience (in years) or leave blank for all realtors: ")
            if experience:
                View_Agency_Related_Realtors_With_Experience(agency_id,experience)
            else:
                View_Agency_Related_Realtors_With_Experience(agency_id,-1)

        elif choice == 7:
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    connect_mysql()
    user_type = input("Enter what kind of user you are: ").strip().lower()

    if user_type == "client":
        handle_client()
    elif user_type == "govt":
        handle_govt()
    elif user_type == "developer":
        handle_developers()
    elif user_type == "realtor agency":
        handle_realtor_agency()
    else:
        print("Unknown user type")

if __name__ == "__main__":
    main()