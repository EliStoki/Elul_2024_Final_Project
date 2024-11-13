from models.employee import Employee
from models.department import Department
from presenters.main_window_presenter import MainWindowPresenter

class EmployeePresenter:
    def __init__(self, model, list_view, add_edit_view, main_window_presenter : MainWindowPresenter):
        self.model = model
        self.list_view = list_view
        self.add_edit_view = add_edit_view
        self.main_window_presenter = main_window_presenter
        self.main_window_presenter.add_panel(self.add_edit_view)

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
        self.main_window_presenter.load_panel(self.add_edit_view)

    def save_employee(self, name, position, dept_name):
        department = Department(dept_id=None, deptName=dept_name)  # Mock department
        employee = Employee(name, age=None, address=None, employee_id=None, position=position, department=department, image_url=None, permission=None)
        self.model.append(employee)
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)
    
    def delete_employee(self, employee):
        self.model.remove(employee)
        self.load_data()

