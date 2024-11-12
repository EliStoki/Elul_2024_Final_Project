import requests
import json
from models.person import Person

class DataAccess:
    def __init__(self):
        self.base_url = "http://localhost:5134/api"

    # Create (POST)
    def create(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return response.json()  # Assuming server returns the created object as JSON
        else:
            response.raise_for_status()

    # Read (GET)
    def read(self, endpoint, resource_id=None):
        url = f"{self.base_url}/{endpoint}"
        if resource_id:
            url += f"/{resource_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            response.raise_for_status()

    # Update (PUT)
    def update(self, endpoint, resource_id, data):
        url = f"{self.base_url}/{endpoint}/{resource_id}"
        json_data = json.dumps(data)  # Convert the data to JSON format
        print(f"Updating data at {url} with payload: {json_data}")  # For debugging
        
        headers = {"Content-Type": "application/json", "accept" : "*/*"}  # Set the header explicitly
        response = requests.put(url, data=json_data, headers=headers)
        
        if response.status_code == 200:
            return True
        else:
            response.raise_for_status()

    # Delete (DELETE)
    def delete(self, endpoint, resource_id):
        url = f"{self.base_url}/{endpoint}/{resource_id}"
        response = requests.delete(url)
        if response.status_code == 204:  # No content after deletion
            return {"message": "Resource deleted successfully"}
        else:
            response.raise_for_status()


# # Example usage:

if __name__ == "__main__":
    base_url = "http://localhost:5134/api"  # Replace with actual server URL
    api = DataAccess(base_url)

    persons = api.read("person")
    print("Persons:", persons)
    # Parse JSON response
    data = json.loads(persons)

    # Convert each dictionary in JSON response to a Person object
    people = [Person(**person) for person in data]

    # Output the result
    for person in people:
        print(person)

    # # Create a new resource
    # new_data = {"name": "John", "age": 30}
    # created_resource = api.create("employees", new_data)
    # print("Created:", created_resource)

    # # Read the created resource
    # employee_id = created_resource["id"]
    # fetched_resource = api.read("employees", employee_id)
    # print("Fetched:", fetched_resource)

    # # Update the resource
    # update_data = {"name": "John Doe", "age": 31}
    # updated_resource = api.update("employees", employee_id, update_data)
    # print("Updated:", updated_resource)

    # # Delete the resource
    # delete_response = api.delete("employees", employee_id)
    # print(delete_response)
