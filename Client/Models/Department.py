# Department model class representing a department within the organization.
class Department:
    def __init__(self, id, deptName):
        """
        Initialize a department with a name and unique identifier.
        :param dept_id: Unique identifier for the department
        :param dept_name: Name of the department
        """
        self.id = id
        self.deptName = deptName

