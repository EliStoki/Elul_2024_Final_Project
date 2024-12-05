import requests
from PySide6.QtCore import QObject, Signal, Slot
from models.employee_da import EmployeeDA
from models.department_da import DepartmentDA
from models.permission_da import PermissionDA

class DataAccessWorker(QObject):
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
        # try:
        if self.operation == 'get_all_employees':
            employees = self.employee_model.get_all()
            employees_and_departments = []
            for employee in employees:
                department = self.dept_model.get(employee.department_id)
                url_content = None
                try:
                    url_response = requests.get(employee.imageUrl)
                    url_content = url_response.content
                except Exception as e:
                    print(f"Error loading image: {e}")
                employees_and_departments.append((employee, department.deptName, url_content))
            self.employees_retrieved.emit(employees_and_departments)
        
        elif self.operation == 'get_all_departments_and_permissions':
            departments = self.dept_model.get_all()
            permissions = self.permission_model.get_all()
            self.departments_and_permissions_retrieved.emit([departments, permissions])
        
        elif self.operation == 'add_employee':
            employee, image_path = self.args
            self.employee_model.add(employee, image_path)
            self.operation = 'get_all_employees'
            self.run()
        
        elif self.operation == 'update_employee':
            employee = self.args
            self.employee_model.update(employee)
            self.employee_operation_complete.emit()
        
        elif self.operation == 'delete_employee':
            employee = self.args
            self.employee_model.delete(employee)
            self.operation = 'get_all_employees'
            self.run()
        
        
        self.finished.emit()
        # except Exception as e:
        #     error_message = f"Database Error: {str(e)}\n{traceback.format_exc()}"
        #     self.error.emit(error_message)