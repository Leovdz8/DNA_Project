import pymysql
# # Global variables for connection and cursor
# connection = None
# cursor = None

# # Function to connect to the database
# def connect_to_database():
#     global connection, cursor
#     try:
#         connection = pymysql.connect(
#             host="localhost",  # Change to your database host
#             user="root",  # Replace with your database username
#             password="rlewandowski9",  # Replace with your database password
#             database="real_estate"  # Replace with your database name
#         )
#         cursor = connection.cursor()
#         print("Connected to the database successfully.")
#     except Exception as e:
#         print("Error connecting to the database:", e)

# # Function to close the database connection
# def close_database_connection():
#     global connection, cursor
#     try:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()
#         print("Database connection closed.")
#     except Exception as e:
#         print("Error closing the database connection:", e)

# Function to add a developer
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
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # Execute the query with provided values
        cursor.execute(query, (
            license_no, name, expiry_date, no_of_projects,
            revenue_first, revenue_second, revenue_third,
            revenue_fourth, revenue_fifth
        ))
        
        # Commit the transaction
        
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
        #   connection.commit()
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
        
        # Commit the transaction
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
            INSERT INTO properties_included (vid, license, pid, owner_id, property_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(properties_included_query, (
            vid, license, pid, owner_id, property_id
        ))

        # Commit the transaction
        # connection.commit()
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
