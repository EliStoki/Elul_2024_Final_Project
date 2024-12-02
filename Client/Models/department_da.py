from DA.DataAccess import DataAccess
from models.department import Department

class DepartmentDA:
    def __init__(self):
        # Initialize the DataAccess API to interact with the database
        self.api = DataAccess()

    def get_all(self):
        # Retrieve all departments from the database and convert each to a Department instance
        departments = self.api.read("department")
        return [Department(**department) for department in departments]

    def get(self, department_id):
        # Retrieve a specific department by ID and convert it to a Department instance
        department = self.api.read("department", department_id)
        return Department(**department) if department else None

    def add(self, department: Department):
        # Convert the Department object to a dictionary and add it to the database
        data = department.to_dict()
        return self.api.create("department", data)

    def update(self, department: Department):
        # Convert the Department object to a dictionary and update the entry in the database
        data = department.to_dict()
        return self.api.update("department", department.id, data)

    def delete(self, department: Department):
        # Delete the department entry in the database using its ID
        return self.api.delete("department", department.id)
