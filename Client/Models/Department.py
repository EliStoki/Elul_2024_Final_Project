# Department model class representing a department within the organization.
class Department:
    def __init__(self, id, deptName):
        self.id = id
        self.deptName = deptName

    def __repr__(self):
        return self.deptName

    def to_dict(self):
        return {
            "id": self.id,
            "deptName": self.deptName
        }

