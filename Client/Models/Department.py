# Department model class representing a department within the organization.
class Department:
    def __init__(self, dept_name, dept_id):
        """
        Initialize a department with a name and unique identifier.
        :param dept_name: Name of the department
        :param dept_id: Unique identifier for the department
        """
        self.dept_name = dept_name
        self.dept_id = dept_id
