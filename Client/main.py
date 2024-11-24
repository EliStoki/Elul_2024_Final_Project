import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from views.person_list_panel import PersonListPanel
from views.person_add_panel import PersonAddPanel
from views.person_edit_panel import PersonEditPanel
from views.employee_list_panel import EmployeeListPanel
from views.employee_add_panel import EmployeeAddPanel
from views.employee_edit_panel import EmployeeEditPanel
from views.department_list_panel import DepartmentListPanel
from views.department_add_panel import DepartmentAddPanel
from views.department_edit_panel import DepartmentEditPanel
from views.permission_list_panel import PermissionListPanel
from views.permission_add_panel import PermissionAddPanel
from views.permission_edit_panel import PermissionEditPanel
from presenters.person_presenter import PersonPresenter
from presenters.employee_presenter import EmployeePresenter
from presenters.department_presenter import DepartmentPresenter
from presenters.permission_presenter import PermissionPresenter
from presenters.main_window_presenter import MainWindowPresenter
from models.person_da import PersonDA
from models.permission_da import PermissionDA
from models.department_da import DepartmentDA
from models.employee_da import EmployeeDA
from models.mock_employee_da import MockEmployeeDA

def main():
    # Create the application instance
    app = QApplication(sys.argv)
    
    # Initialize the main window
    main_window = MainWindow()
    
    # Initialize models
    person_model = PersonDA()
    employee_model = EmployeeDA()
    department_model = DepartmentDA()
    permission_model = PermissionDA()
    
        
    # Initialize main window presenter
    main_window_presenter = MainWindowPresenter(main_window)

    # Initialize person views
    person_list_view = PersonListPanel()
    person_add_view = PersonAddPanel()
    person_edit_view = PersonEditPanel()

    # Initialize employee views
    employee_list_view = EmployeeListPanel()
    employee_add_view = EmployeeAddPanel()
    employee_edit_view = EmployeeEditPanel()
    
    # Initialize department views
    department_list_view = DepartmentListPanel()
    department_add_view = DepartmentAddPanel()
    department_edit_view = DepartmentEditPanel()

    # Initialize permission views
    permission_list_view = PermissionListPanel()
    permission_add_view = PermissionAddPanel()
    permission_edit_view = PermissionEditPanel()

    # Add views to the main window's panels area stack
    main_window_presenter.add_panel(person_list_view)
    main_window_presenter.add_panel(employee_list_view)
    main_window_presenter.add_panel(department_list_view)
    main_window_presenter.add_panel(permission_list_view)
    main_window_presenter.add_panel(person_add_view)
    main_window_presenter.add_panel(person_edit_view)
    main_window_presenter.add_panel(employee_add_view)
    main_window_presenter.add_panel(employee_edit_view)
    main_window_presenter.add_panel(department_add_view)
    main_window_presenter.add_panel(department_edit_view)
    main_window_presenter.add_panel(permission_add_view)
    main_window_presenter.add_panel(permission_edit_view)

    # Initialize presenters
    person_presenter = PersonPresenter(person_model, person_list_view, person_add_view, person_edit_view, main_window_presenter)
    employee_presenter = EmployeePresenter(employee_model, department_model, permission_model, employee_list_view, employee_add_view, employee_edit_view,  main_window_presenter)
    department_presenter = DepartmentPresenter(department_model, department_list_view, department_add_view, department_edit_view, main_window_presenter)
    permission_presenter = PermissionPresenter(permission_model, permission_list_view, permission_add_view, permission_edit_view, main_window_presenter)

    # Show the main window
    main_window_presenter.run()
    
    # Run the application event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
