import requests

class DataAccess:
    def __init__(self):
        base_url = base_url

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
        else:
            response.raise_for_status()

    # Update (PUT)
    def update(self, endpoint, resource_id, data):
        url = f"{self.base_url}/{endpoint}/{resource_id}"
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return response.json()
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

# if __name__ == "__main__":
#     base_url = "https://api.example.com"  # Replace with actual server URL
#     api = DataAccess(base_url)

#     # Create a new resource
#     new_data = {"name": "John", "age": 30}
#     created_resource = api.create("employees", new_data)
#     print("Created:", created_resource)

#     # Read the created resource
#     employee_id = created_resource["id"]
#     fetched_resource = api.read("employees", employee_id)
#     print("Fetched:", fetched_resource)

#     # Update the resource
#     update_data = {"name": "John Doe", "age": 31}
#     updated_resource = api.update("employees", employee_id, update_data)
#     print("Updated:", updated_resource)

#     # Delete the resource
#     delete_response = api.delete("employees", employee_id)
#     print(delete_response)
