class Employee:
    def __init__(self, emp_id, name, department, role, photo):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.role = role
        self.photo = photo

class EmployeeModel:
    def __init__(self):
        # A dictionary to simulate a database
        self.employees = {}

    def add_employee(self, emp_id, name, department, role, photo):
        employee = Employee(emp_id, name, department, role, photo)
        self.employees[emp_id] = employee

    def get_employee(self, emp_id):
        return self.employees.get(emp_id)

    def update_employee(self, emp_id, name=None, department=None, role=None, photo=None):
        employee = self.get_employee(emp_id)
        if employee:
            if name:
                employee.name = name
            if department:
                employee.department = department
            if role:
                employee.role = role
            if photo:
                employee.photo = photo

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]

    def get_all_employees(self):
        return list(self.employees.values())
