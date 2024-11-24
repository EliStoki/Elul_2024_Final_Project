from models.employee import Employee
from models.department import Department
from models.permission import Permission
from presenters.main_window_presenter import MainWindowPresenter
from models.employee_da import EmployeeDA
from models.department_da import DepartmentDA
from models.permission_da import PermissionDA

class EmployeePresenter:
    def __init__(self, model: EmployeeDA, dept_da : DepartmentDA, permission_da : PermissionDA, list_view, add_view, edit_view, main_window_presenter: MainWindowPresenter):
        self.model = model
        self.dept_da = dept_da
        self.permission_da = permission_da
        self.list_view = list_view
        self.add_view = add_view
        self.edit_view = edit_view
        self.main_window_presenter = main_window_presenter

        # Set presenter for views
        self.list_view.set_presenter(self)
        self.add_view.set_presenter(self)
        self.edit_view.set_presenter(self)

        # Load initial data
        self.load_data()

    def load_data(self):
        """Load data into the list view."""
        self.list_view.clear()
        for employee in self.model.get_all():
            self.list_view.add_item(employee)

    def open_add_view(self):
        """Prepare and display the Add View."""
        self.add_view.name_input.clear()
        self.add_view.position_input.clear()
        self.add_view.dept_input.clear()
        self.main_window_presenter.load_panel(self.add_view)

    def open_edit_view(self, employee: Employee):
        """Prepare and display the Edit View with the selected employee's data."""
        self.edit_view.edited_employee = employee.id
        self.edit_view.name_input.setText(employee.name)
        self.edit_view.position_input.setText(employee.position)
        self.edit_view.department_input.clear()
        for dept in self.dept_da.get_all():
            self.edit_view.department_input.addItem(dept.deptName, dept)
        self.edit_view.permission_input.clear()
        for permission in self.permission_da.get_all():
            self.edit_view.permission_input.addItem(str(permission.id), permission)
        self.edit_view.department_input.setCurrentText(employee.department.deptName)
        self.main_window_presenter.load_panel(self.edit_view)

    def add_employee(self, id, name, position, dept_name):
        """Add a new employee."""
        try:
            department = Department(id=None, deptName=dept_name)  # Mock department object
            employee = Employee(
                id=int(id),
                name=name,
                position=position,
                department=department
            )
            self.model.add(employee)
        except ValueError as e:
            print(f"Error converting ID to integer: {e}")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)

    def update_employee(self, id, name, position, department, permission):
        employee = self.model.get(id)
        """Update an existing employee."""
        try:
            employee = Employee(
                id=int(id),
                name=name,
                position=position,
                department=department,
                imageUrl=employee.imageUrl,
                address=employee.address,
                permission=permission,
                age=employee.age
            )
            self.model.update(employee)
        except ValueError as e:
            print(f"Error converting ID to integer: {e}")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)

    def delete_employee(self, employee):
        """Delete the selected employee."""
        self.model.delete(employee)
        self.load_data()

    def open_list_view(self):
        """Display the list view."""
        self.main_window_presenter.load_panel(self.list_view)

    def filter_table(self):
        """Filter the table rows based on the search bar text and selected column."""
        search_text = self.list_view.search_bar.text().lower()
        selected_column = self.list_view.filter_dropdown.currentIndex()  # Get selected column index

        for row in range(self.list_view.table.rowCount()):
            item = self.list_view.table.item(row, selected_column)
            if item and search_text in item.text().lower():
                self.list_view.table.showRow(row)
            else:
                self.list_view.table.hideRow(row)