from models.person import Person
from models.department import Department
from models.permission import Permission

# Employee model class, extending Person with additional employee-specific attributes.

class Employee(Person):
    def __init__(self, id, name, age, address, position, department, imageUrl, permission):
        super().__init__(id, name, age, address)
        self.position = position
        self.department: Department = Department(**department) if isinstance(department, dict) else department
        self.imageUrl = imageUrl
        self.permission: Permission = Permission(**permission) if isinstance(permission, dict) else permission

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "employeeId": self.id,
            "position": self.position,
            "department": self.department.to_dict(),
            "imageUrl": self.imageUrl,
            "permission": self.permission.to_dict()
        }

