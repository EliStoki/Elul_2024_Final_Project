import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from views.person_list_panel import PersonListPanel
from views.person_add_edit_panel import PersonAddEditPanel
from views.employee_list_panel import EmployeeListPanel
from views.employee_add_edit_panel import EmployeeAddEditPanel
from views.department_list_panel import DepartmentListPanel
from views.department_add_edit_panel import DepartmentAddEditPanel
from views.permission_list_panel import PermissionListPanel
from views.permission_add_edit_panel import PermissionAddEditPanel
from presenters.person_presenter import PersonPresenter
from presenters.employee_presenter import EmployeePresenter
from presenters.department_presenter import DepartmentPresenter
from presenters.permission_presenter import PermissionPresenter
from models.person import Person
from models.employee import Employee
from models.department import Department
from models.permission import Permission

def main():
    # Create the application instance
    app = QApplication(sys.argv)
    
    # Initialize the main window
    main_window = MainWindow()
    
    # Initialize models
    person_model = []
    employee_model = []
    department_model = []
    permission_model = []
    
    # Initialize person views and presenter
    person_list_view = PersonListPanel()
    person_add_edit_view = PersonAddEditPanel()
    person_presenter = PersonPresenter(person_model, person_list_view, person_add_edit_view)
    
    # Initialize employee views and presenter
    employee_list_view = EmployeeListPanel()
    employee_add_edit_view = EmployeeAddEditPanel()
    employee_presenter = EmployeePresenter(employee_model, employee_list_view, employee_add_edit_view)
    
    # Initialize department views and presenter
    department_list_view = DepartmentListPanel()
    department_add_edit_view = DepartmentAddEditPanel()
    department_presenter = DepartmentPresenter(department_model, department_list_view, department_add_edit_view)
    
    # Initialize permission views and presenter
    permission_list_view = PermissionListPanel()
    permission_add_edit_view = PermissionAddEditPanel()
    permission_presenter = PermissionPresenter(permission_model, permission_list_view, permission_add_edit_view)
    
    # Add views to the main window's main area stack
    main_window.main_area.addWidget(person_list_view)
    main_window.main_area.addWidget(employee_list_view)
    main_window.main_area.addWidget(department_list_view)
    main_window.main_area.addWidget(permission_list_view)
    
    # Show the main window
    main_window.show()
    
    # Run the application event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
