from queue import Queue
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMessageBox
from models.employee import Employee
from models.employee_da import EmployeeDA
from models.department_da import DepartmentDA
from models.permission_da import PermissionDA
from presenters.main_window_presenter import MainWindowPresenter
from presenters.data_access_worker import DataAccessWorker

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

        self.next_to_run = Queue()

        # Threading setup
        self.thread = QThread()
        self.database_worker = DataAccessWorker(self.model, self.dept_da, self.permission_da)
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

        self.status_text = "Loading data..."

        # Load initial data
        self.load_data()

    def _start_database_operation(self, operation: str, args=None):
        """
        Start a database operation in a separate thread.

        :param operation: Name of the database operation to perform
        :param args: Arguments for the database operation
        """
        if self.thread.isRunning():
            self.next_to_run.put((operation, args))
            return

        self.database_worker.operation = operation
        self.database_worker.args = args
        self.thread.start()

    def _handle_database_error(self, error_message: str):
        """
        Handle and display database errors.

        :param error_message: Detailed error message
        """
        print(f"{error_message} from error handler")
        self.status_text = f"{error_message}"

    def load_data(self):
        """Load employees asynchronously with departments."""
        self.list_view.clear()
        self.list_view.loading(True)
        self.main_window_presenter.set_status_bar_text("Loading Employees...")
        self._start_database_operation('get_all_employees')
        self.status_text = "Employees loaded successfully."

    def _on_employees_retrieved(self, employees):
        """
        Handle retrieved employees and update the list view.

        :param employees: List of retrieved employees
        """
        self.list_view.clear()
        for employee in employees:
            # Retrieve department name asynchronously
            self.list_view.add_item(employee[0], employee[1], employee[2])
        self.list_view.loading(False)
        self.main_window_presenter.set_status_bar_text(self.status_text)

    def _on_department_and_permissions_retrieved(self, departments_and_permissions):
        """
        Add department details to matching employee in list view.

        :param departments: List of retrieved departments
        """

        self.add_view.department_input.clear()
        self.add_view.permission_input.clear()

        for department in departments_and_permissions[0]:
            self.add_view.department_input.addItem(department.deptName, department)

        for permission in departments_and_permissions[1]:
            self.add_view.permission_input.addItem(str(permission.id), permission)

    def _on_employee_operation_complete(self):
        """Refresh the list view after a database operation."""                
        self.list_view.loading(False)
        self.main_window_presenter.set_status_bar_text(self.status_text)

        if not self.next_to_run.empty():
            operation, args = self.next_to_run.get()
            self._start_database_operation(operation, args)


    
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
            self.list_view.loading(True)
            self.main_window_presenter.set_status_bar_text(f"Adding {name}...")
            self.main_window_presenter.load_panel(self.list_view)
            self._start_database_operation('add_employee', (employee, image_path))
            self.status_text = f"Employee {name} added successfully."
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
            self.main_window_presenter.set_status_bar_text(f"Employee {name} updated successfully.")
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
        self.list_view.loading(True)
        self.main_window_presenter.set_status_bar_text(f"Deliting  {employee.name}...")
        self._start_database_operation('delete_employee', employee)
        self.status_text = f"Employee {employee.name} deleted successfully."

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