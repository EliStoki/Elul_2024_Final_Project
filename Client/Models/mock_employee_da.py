from models.employee import Employee
from models.department import Department
from models.permission import Permission

class MockEmployeeDA:
    def __init__(self):
        # Initialize mock data for departments and permissions
        self.departments = [
            Department(1, "HR"),
            Department(2, "Finance"),
            Department(3, "Engineering"),
            Department(4, "Marketing"),
            Department(5, "IT Support")
        ]

        self.permissions = [
            Permission(1, "Ground Floor", "Main Building"),
            Permission(2, "2nd Floor", "Finance Building"),
            Permission(3, "3rd Floor", "Tech Building"),
            Permission(4, "4th Floor", "Marketing Wing"),
            Permission(5, "Basement", "IT Center")
        ]

        # Initialize mock data for employees
        self.employees = [
            Employee(1, "Alice Johnson", 30, "123 Main St", 101, "HR Manager", self.departments[0], "images/alice.jpg", self.permissions[0]),
            Employee(2, "Bob Smith", 25, "456 Oak Ave", 102, "Software Engineer", self.departments[2], "images/bob.jpg", self.permissions[2]),
            Employee(3, "Charlie Brown", 28, "789 Pine Rd", 103, "Accountant", self.departments[1], "images/charlie.jpg", self.permissions[1]),
            Employee(4, "Diana Ross", 35, "321 Elm St", 104, "Marketing Lead", self.departments[3], "images/diana.jpg", self.permissions[3]),
            Employee(5, "Ethan Hunt", 32, "654 Maple Ln", 105, "IT Specialist", self.departments[4], "images/ethan.jpg", self.permissions[4]),
            Employee(6, "Fiona Adams", 29, "987 Cedar Ct", 106, "Recruiter", self.departments[0], "images/fiona.jpg", self.permissions[0]),
            Employee(7, "George Clark", 40, "159 Birch Blvd", 107, "Finance Director", self.departments[1], "images/george.jpg", self.permissions[1]),
            Employee(8, "Hannah Lee", 27, "753 Willow Way", 108, "Frontend Developer", self.departments[2], "images/hannah.jpg", self.permissions[2]),
            Employee(9, "Isaac Newton", 33, "246 Aspen St", 109, "System Analyst", self.departments[4], "images/isaac.jpg", self.permissions[4]),
            Employee(10, "Julia Roberts", 38, "369 Spruce Dr", 110, "PR Specialist", self.departments[3], "images/julia.jpg", self.permissions[3])
        ]

    def get_all(self):
        # Return all mock employees
        return self.employees

    def get(self, employee_id):
        # Return a specific employee by ID or None if not found
        return next((employee for employee in self.employees if employee.employee_id == employee_id), None)

    def add(self, employee: Employee):
        # Add a new employee to the mock data
        self.employees.append(employee)
        return employee

    def update(self, employee: Employee):
        # Find and update the employee with the given ID
        for idx, existing_employee in enumerate(self.employees):
            if existing_employee.employee_id == employee.employee_id:
                self.employees[idx] = employee
                return employee
        return None

    def delete(self, employee: Employee):
        # Remove the employee from the mock data
        self.employees = [e for e in self.employees if e.employee_id != employee.employee_id]
        return employee
