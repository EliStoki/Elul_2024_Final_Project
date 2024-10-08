class EmployeeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Connect signals and slots
        self.view.add_button.clicked.connect(self.add_employee)
        self.view.update_button.clicked.connect(self.update_employee)
        self.view.delete_button.clicked.connect(self.delete_employee)
        self.view.load_button.clicked.connect(self.load_employee)
        self.view.employee_list.itemClicked.connect(self.display_employee_details)

        # Load initial employee list
        self.update_employee_list()

    def add_employee(self):
        name, department, role, photo = self.view.get_employee_details()
        emp_id = str(len(self.model.employees) + 1)
        self.model.add_employee(emp_id, name, department, role, photo)
        self.view.clear_inputs()
        self.update_employee_list()

    def update_employee(self):
        emp_id = self.view.employee_list.currentItem().text().split(" ")[0]
        name, department, role, photo = self.view.get_employee_details()
        self.model.update_employee(emp_id, name, department, role, photo)
        self.update_employee_list()

    def delete_employee(self):
        emp_id = self.view.employee_list.currentItem().text().split(" ")[0]
        self.model.delete_employee(emp_id)
        self.view.clear_inputs()
        self.update_employee_list()

    def load_employee(self):
        emp_id = self.view.employee_list.currentItem().text().split(" ")[0]
        employee = self.model.get_employee(emp_id)
        if employee:
            self.view.set_employee_details(employee.name, employee.department, employee.role, employee.photo)

    def display_employee_details(self):
        self.load_employee()

    def update_employee_list(self):
        self.view.employee_list.clear()
        for employee in self.model.get_all_employees():
            self.view.employee_list.addItem(f"{employee.emp_id} {employee.name} - {employee.department} - {employee.role}")
