from DA.DataAccess import DataAccess
from models.employee import Employee

class EmployeeDA:
    def __init__(self):
        # Initialize the DataAccess API to interact with the database
        self.api = DataAccess()

    def get_all(self):
        # Retrieve all employees from the database and convert each to an Employee instance
        employees = self.api.read("employee")
        return [Employee(**employee) for employee in employees]

    def get(self, employee_id):
        # Retrieve a specific employee by ID and convert it to an Employee instance
        employee = self.api.read("employee", employee_id)
        return Employee(**employee) if employee else None

    def add(self, employee: Employee):
        # Convert the Employee object to a dictionary and add it to the database
        data = employee.to_dict()
        return self.api.create("employee", data)

    def update(self, employee: Employee):
        # Convert the Employee object to a dictionary and update the entry in the database
        data = employee.to_dict()
        return self.api.update("employee", employee.id, data)

    def delete(self, employee: Employee):
        # Delete the employee entry in the database using its ID
        return self.api.delete("employee", employee.id)
