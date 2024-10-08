class Employee(Person):
    def __init__(self, name, age, address, employee_id, position, department, image_url, permission):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.position = position
        self.department = department  # This is a Department object
        self.image_url = image_url
        self.permission = permission # Permission object
        
    def __str__(self):
        return (f"{super().__str__()}, Employee ID: {self.employee_id}, "
                f"Position: {self.position}, {self.department}")