import traceback
from typing import List, Optional

from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QMessageBox

from models.department import Department
from models.department_da import DepartmentDA
from presenters.main_window_presenter import MainWindowPresenter

class DatabaseWorker(QObject):
    """
    Worker class to perform database operations in a separate thread.
    Uses signals to communicate results back to the main thread.
    """
    # Signals for different database operations
    finished = Signal()
    error = Signal(str)
    departments_retrieved = Signal(list)
    department_operation_complete = Signal()

    def __init__(self, model: DepartmentDA):
        """
        Initialize the worker with a database access model.

        :param model: Data access layer for departments
        """
        super().__init__()
        self.model = model
        self.operation = None
        self.args = None

    @Slot()
    def run(self):
        """
        Execute the specified database operation.
        Handles different operations based on the stored method and arguments.
        """
        try:
            if self.operation == 'get_all':
                departments = self.model.get_all()
                self.departments_retrieved.emit(departments)
            elif self.operation == 'add':
                self.model.add(self.args)
                self.department_operation_complete.emit()
            elif self.operation == 'update':
                self.model.update(self.args)
                self.department_operation_complete.emit()
            elif self.operation == 'delete':
                self.model.delete(self.args)
                self.department_operation_complete.emit()
            
            self.finished.emit()
        except Exception as e:
            error_message = f"Database Error: {str(e)}\n{traceback.format_exc()}"
            self.error.emit(error_message)

class DepartmentPresenter:
    def __init__(self, model: DepartmentDA, list_view, add_view, edit_view, main_window_presenter: MainWindowPresenter):
        """
        Initialize the Department Presenter with threading support.

        :param model: Data access layer for departments
        :param list_view: View for listing departments
        :param add_view: View for adding departments
        :param edit_view: View for editing departments
        :param main_window_presenter: Main window presenter
        """
        self.model = model
        self.list_view = list_view
        self.add_view = add_view
        self.edit_view = edit_view
        self.main_window_presenter = main_window_presenter

        # Threading setup
        self.thread = QThread()
        self.database_worker = DatabaseWorker(self.model)
        self.database_worker.moveToThread(self.thread)

        # Connect worker signals
        self.thread.started.connect(self.database_worker.run)
        self.database_worker.finished.connect(self.thread.quit)
        self.database_worker.error.connect(self._handle_database_error)
        
        # Operation-specific signal connections
        self.database_worker.departments_retrieved.connect(self._on_departments_retrieved)
        self.database_worker.department_operation_complete.connect(self._on_department_operation_complete)

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
        """Load departments asynchronously."""
        self.list_view.clear()
        self._start_database_operation('get_all')

    def _on_departments_retrieved(self, departments: List[Department]):
        """
        Handle retrieved departments and update the list view.

        :param departments: List of retrieved departments
        """
        for department in departments:
            self.list_view.add_item(department)

    def _on_department_operation_complete(self):
        """Set up the list view after a department operation is complete."""
        self.main_window_presenter.load_panel(self.list_view)

    def open_add_view(self):
        """Prepare and display the Add View."""
        self.add_view.dept_name_input.clear()
        self.add_view.dept_id_input.clear()
        self.main_window_presenter.load_panel(self.add_view)

    def open_edit_view(self, department: Department):
        """
        Prepare and display the Edit View with the selected department's data.

        :param department: Department to be edited
        """
        self.edit_view.edited_department = department.id
        self.edit_view.dept_name_input.setText(department.deptName)
        self.edit_view.dept_id_input.setText(str(department.id))
        self.main_window_presenter.load_panel(self.edit_view)

    def add_department(self, dept_id: str, dept_name: str):
        """
        Add a new department asynchronously.

        :param dept_id: Department ID
        :param dept_name: Department name
        """
        try:
            department = Department(id=int(dept_id), deptName=dept_name)
            self._start_database_operation('add', department)
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

    def update_department(self, dept_id: str, dept_name: str):
        """
        Update an existing department asynchronously.

        :param dept_id: Department ID
        :param dept_name: Department name
        """
        try:
            department = Department(id=int(dept_id), deptName=dept_name)
            self._start_database_operation('update', department)
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

    def delete_department(self, department: Department):
        """
        Delete the selected department asynchronously.

        :param department: Department to be deleted
        """
        self._start_database_operation('delete', department)

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