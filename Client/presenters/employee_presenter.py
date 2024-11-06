from models.employee import Employee
from models.department import Department

class EmployeePresenter:
    def __init__(self, model, list_view, add_edit_view):
        self.model = model
        self.list_view = list_view
        self.add_edit_view = add_edit_view
        
        # Set presenter for views
        self.list_view.set_presenter(self)
        self.add_edit_view.set_presenter(self)
        
        # Load initial data
        self.load_data()

    def load_data(self):
        self.list_view.employee_list.clear()
        for employee in self.model:
            self.list_view.add_item(employee)

    def open_add_edit_view(self, employee=None):
        if employee:
            self.add_edit_view.name_input.setText(employee.name)
            self.add_edit_view.position_input.setText(employee.position)
            self.add_edit_view.dept_input.setText(employee.department.dept_name)
        else:
            self.add_edit_view.name_input.clear()
            self.add_edit_view.position_input.clear()
            self.add_edit_view.dept_input.clear()
        self.add_edit_view.show()

    def save_employee(self, name, position, dept_name):
        department = Department(dept_name, dept_id=None)  # Mock department
        employee = Employee(name, age=None, address=None, employee_id=None, position=position, department=department, image_url=None, permission=None)
        self.model.append(employee)
        self.load_data()
        self.add_edit_view.hide()

    def delete_employee(self, employee):
        self.model.remove(employee)
        self.load_data()
