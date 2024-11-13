import requests
import json
from models.person import Person

class DataAccess:
    def __init__(self):
        self.base_url = "http://localhost:5134/api"

    # Create (POST)
    def create(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        print(f"Creating data at {url} with payload: {data}")  # For debugging
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
        print("Reading data from:", url)  # For debugging
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
        print("Deleting data from:", url)  # For debugging
        response = requests.delete(url)
        if response.status_code == 204:  # No content after deletion
            return {"message": "Resource deleted successfully"}
        else:
            response.raise_for_status()