class Department:
    def __init__(self, dept_name, dept_id):
        self.dept_name = dept_name
        self.dept_id = dept_id
        
    def __str__(self):
        return f"Department: {self.dept_name}, ID: {self.dept_id}"