from models.person import Person
from models.department import Department
from models.permission import Permission

# Employee model class, extending Person with additional employee-specific attributes.
class Employee(Person):
    def __init__(self, id, name, age, address, employee_id, position, department : Department, image_url, permission : Permission):
        """
        Initialize an employee with both personal and job-related attributes.
        :param employee_id: Unique ID for the employee
        :param position: Job title or role of the employee
        :param department: Department object where the employee works
        :param image_url: URL of the employee's image
        :param permission: Permission object specifying access level
        """
        super().__init__(id, name, age, address)
        self.employee_id = employee_id
        self.position = position
        self.department = department  # Link to a Department instance
        self.image_url = image_url
        self.permission = permission  # Link to a Permission instance
