import traceback
from typing import List, Optional

from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QMessageBox

from models.employee import Employee
from models.department import Department
from models.permission import Permission
from models.employee_da import EmployeeDA
from models.department_da import DepartmentDA
from models.permission_da import PermissionDA
from presenters.main_window_presenter import MainWindowPresenter

class DatabaseWorker(QObject):
    """
    Worker class to perform database operations in a separate thread.
    Uses signals to communicate results back to the main thread.
    """
    # Signals for different database operations
    finished = Signal()
    error = Signal(str)
    employees_retrieved = Signal(list)
    departments_and_permissions_retrieved = Signal(list)
    permissions_retrieved = Signal(list)
    employee_operation_complete = Signal()

    def __init__(self, 
                 employee_model: EmployeeDA, 
                 dept_model: DepartmentDA, 
                 permission_model: PermissionDA):
        """
        Initialize the worker with database access models.

        :param employee_model: Data access layer for employees
        :param dept_model: Data access layer for departments
        :param permission_model: Data access layer for permissions
        """
        super().__init__()
        self.employee_model = employee_model
        self.dept_model = dept_model
        self.permission_model = permission_model
        
        self.operation = None
        self.args = None

    @Slot()
    def run(self):
        """
        Execute the specified database operation.
        Handles different operations based on the stored method and arguments.
        """
        try:
            if self.operation == 'get_all_employees':
                employees = self.employee_model.get_all()
                employees_and_departments = []
                for employee in employees:
                    department = self.dept_model.get(employee.department_id)
                    employees_and_departments.append((employee, department.deptName))
                self.employees_retrieved.emit(employees_and_departments)
            
            elif self.operation == 'get_all_departments_and_permissions':
                departments = self.dept_model.get_all()
                permissions = self.permission_model.get_all()
                self.departments_and_permissions_retrieved.emit(departments, permissions)
            
            elif self.operation == 'add_employee':
                employee, image_path = self.args
                self.employee_model.add(employee, image_path)
                self.employee_operation_complete.emit()
            
            elif self.operation == 'update_employee':
                employee = self.args
                self.employee_model.update(employee)
                self.employee_operation_complete.emit()
            
            elif self.operation == 'delete_employee':
                employee = self.args
                self.employee_model.delete(employee)
                self.employee_operation_complete.emit()
            
            
            self.finished.emit()
        except Exception as e:
            error_message = f"Database Error: {str(e)}\n{traceback.format_exc()}"
            self.error.emit(error_message)

class EmployeePresenter:
    def __init__(self, 
                 model: EmployeeDA, 
                 dept_da: DepartmentDA, 
                 permission_da: PermissionDA, 
                 list_view, 
                 add_view, 
                 edit_view, 
                 main_window_presenter: MainWindowPresenter):
        """
        Initialize the Employee Presenter with threading support.

        :param model: Data access layer for employees
        :param dept_da: Data access layer for departments
        :param permission_da: Data access layer for permissions
        :param list_view: View for listing employees
        :param add_view: View for adding employees
        :param edit_view: View for editing employees
        :param main_window_presenter: Main window presenter
        """
        self.model = model
        self.dept_da = dept_da
        self.permission_da = permission_da
        self.list_view = list_view
        self.add_view = add_view
        self.edit_view = edit_view
        self.main_window_presenter = main_window_presenter

        # Threading setup
        self.thread = QThread()
        self.database_worker = DatabaseWorker(self.model, self.dept_da, self.permission_da)
        self.database_worker.moveToThread(self.thread)

        # Connect worker signals
        self.thread.started.connect(self.database_worker.run)
        self.database_worker.finished.connect(self.thread.quit)
        self.database_worker.error.connect(self._handle_database_error)
        
        # Operation-specific signal connections
        self.database_worker.employees_retrieved.connect(self._on_employees_retrieved)
        self.database_worker.departments_and_permissions_retrieved.connect(self._on_department_and_permissions_retrieved)
        self.database_worker.employee_operation_complete.connect(self._on_employee_operation_complete)

        # Set presenter for views
        self.list_view.set_presenter(self)
        self.add_view.set_presenter(self)
        self.edit_view.set_presenter(self)

        # Load initial data
        self.load_data()

    def _start_database_operation(self, operation: str, args=None):
        """
        Start a database operation in a separate thread.

        :param operation: Name of the database operation to perform
        :param args: Arguments for the database operation
        """
        if self.thread.isRunning():
            return

        self.database_worker.operation = operation
        self.database_worker.args = args
        self.thread.start()

    def _handle_database_error(self, error_message: str):
        """
        Handle and display database errors.

        :param error_message: Detailed error message
        """
        QMessageBox.critical(
            self.list_view, 
            "Database Error", 
            f"An error occurred during database operation:\n{error_message}"
        )

    def load_data(self):
        """Load employees asynchronously with departments."""
        self.list_view.clear()
        self._start_database_operation('get_all_employees')

    def _on_employees_retrieved(self, employees):
        """
        Handle retrieved employees and update the list view.

        :param employees: List of retrieved employees
        """
        for employee in employees:
            # Retrieve department name asynchronously
            self.list_view.add_item(employee[0], employee[1])

    def _on_department_and_permissions_retrieved(self, departments, permissions):
        """
        Add department details to matching employee in list view.

        :param departments: List of retrieved departments
        """
        for department in departments:
            self.add_view.department_input.addItem(department.deptName, department)

        for permission in permissions:
            self.add_view.permission_input.addItem(permission.permissionName, permission)

    def _on_employee_operation_complete(self):
        """Refresh the list view after a database operation."""
        self.main_window_presenter.load_panel(self.list_view)

    def open_add_view(self):
        """Prepare and display the Add View."""
        self.add_view.name_input.clear()
        self.add_view.age_input.clear()
        self.add_view.address_input.clear()
        self.add_view.position_input.clear()
        self.add_view.image_input.clear()

        # Load departments and permissions asynchronously
        self._start_database_operation('get_all_departments_and_permissions')

        self.main_window_presenter.load_panel(self.add_view)

    def open_edit_view(self, employee: Employee):
        """
        Prepare and display the Edit View with the selected employee's data.

        :param employee: Employee to be edited
        """
        self.edit_view.edited_employee = employee.id
        self.edit_view.name_input.setText(employee.name)
        self.edit_view.position_input.setText(employee.position)

        # Load departments and permissions asynchronously
        self._start_database_operation('get_all_departments')
        self._start_database_operation('get_all_permissions')

        self.main_window_presenter.load_panel(self.edit_view)

    def add_employee(self, name, age, address, position, dept, permission, image_path):
        """
        Add a new employee asynchronously.

        :param name: Employee name
        :param age: Employee age
        :param address: Employee address
        :param position: Employee position
        :param dept: Department ID
        :param permission: Permission ID
        :param image_path: Path to employee image
        """
        try:
            employee = Employee(
                id=0,
                name=name,
                age=age,
                address=address,
                position=position,
                department=int(dept),
                imageUrl="",
                permission=int(permission)
            )
            self._start_database_operation('add_employee', (employee, image_path))
        except ValueError as e:
            QMessageBox.warning(
                self.add_view, 
                "Invalid Input", 
                f"Error converting ID to integer: {e}"
            )
        except Exception as e:
            QMessageBox.critical(
                self.add_view, 
                "Error", 
                f"An error occurred: {e}"
            )

    def update_employee(self, id, name, position, department, permission):
        """
        Update an existing employee asynchronously.

        :param id: Employee ID
        :param name: Employee name
        :param position: Employee position
        :param department: Department ID
        :param permission: Permission ID
        """
        try:
            # First, retrieve the existing employee to preserve other details
            employee = self.model.get(id)
            updated_employee = Employee(
                id=int(id),
                name=name,
                position=position,
                department=department,
                imageUrl=employee.imageUrl,
                address=employee.address,
                permission=permission,
                age=employee.age
            )
            self._start_database_operation('update_employee', updated_employee)
        except ValueError as e:
            QMessageBox.warning(
                self.edit_view, 
                "Invalid Input", 
                f"Error converting ID to integer: {e}"
            )
        except Exception as e:
            QMessageBox.critical(
                self.edit_view, 
                "Error", 
                f"An error occurred: {e}"
            )

    def delete_employee(self, employee):
        """
        Delete the selected employee asynchronously.

        :param employee: Employee to be deleted
        """
        self._start_database_operation('delete_employee', employee)

    def open_list_view(self):
        """Display the list view."""
        self.main_window_presenter.load_panel(self.list_view)

    def filter_table(self):
        """Filter the table rows based on the search bar text and selected column."""
        search_text = self.list_view.search_bar.text().lower()
        selected_column = self.list_view.filter_dropdown.currentIndex()

        for row in range(self.list_view.table.rowCount()):
            item = self.list_view.table.item(row, selected_column)
            if item and search_text in item.text().lower():
                self.list_view.table.showRow(row)
            else:
                self.list_view.table.hideRow(row)