import pyodbc
import json

# Connection to the SQL Server database hosted on somee.com
def connect_to_database():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=FINAL-ELUL-2024-PROJECT.mssql.somee.com;'
            'DATABASE=FINAL-ELUL-2024-PROJECT;'
            'UID=elis_SQLLogin_1;'
            'PWD=n5tq8n1kzs;'
        )
        print("Connection successful!")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Execute the query and return data in JSON format
def fetch_data_as_json():
    connection = connect_to_database()
    
    if not connection:
        return None
    
    try:
        cursor = connection.cursor()
        # Write your SQL query here
        query = "SELECT * FROM Employee"  # Example query to fetch data from Employee table
        cursor.execute(query)
        
        # Fetch all rows
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        # Convert the result to a list of dictionaries
        result = [dict(zip(columns, row)) for row in rows]
        
        # Convert the result to JSON format
        result_json = json.dumps(result, indent=4)
        print("Query executed successfully!")
        return result_json
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        connection.close()

# Store the result in a JSON file
def save_to_json_file(data, filename="result.json"):
    try:
        with open(filename, 'w') as json_file:
            json_file.write(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Main function
if __name__ == "__main__":
    data_json = fetch_data_as_json()
    if data_json:
        print(data_json)
