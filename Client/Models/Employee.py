from models.person import Person
from models.department import Department
from models.permission import Permission

# Employee model class, extending Person with additional employee-specific attributes.

class Employee(Person):
    def __init__(self, position, department, imageUrl, permission, id, name, age, address):
        super().__init__(id, name, age, address)
        self.position = position
        self.department_id = department
        self.imageUrl = imageUrl
        self.permission_id = permission

    def to_dict(self):
        return super().to_dict() | {
            "Position": self.position,
            "Department": self.department_id,
            "ImageUrl": "Url",
            "Permission": self.permission_id
        }

