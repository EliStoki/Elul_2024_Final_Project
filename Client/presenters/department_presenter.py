from models.department import Department
from presenters.main_window_presenter import MainWindowPresenter
from models.department_da import DepartmentDA

class DepartmentPresenter:
    def __init__(self, model : DepartmentDA, list_view, add_edit_view, main_window_presenter : MainWindowPresenter):
        self.model = model
        self.list_view = list_view
        self.add_edit_view = add_edit_view
        self.main_window_presenter = main_window_presenter

        # Set presenter for views
        self.list_view.set_presenter(self)
        self.add_edit_view.set_presenter(self)
        
        # Load initial data
        self.load_data()

    def load_data(self):
        self.list_view.clear()
        for department in self.model.get_all():
            self.list_view.add_item(department)

    def open_add_edit_view(self, department=None):
        if department:
            self.add_edit_view.dept_name_input.setText(department.deptName)
            self.add_edit_view.dept_id_input.setText(str(department.id))
        else:
            self.add_edit_view.dept_name_input.clear()
            self.add_edit_view.dept_id_input.clear()
        
        self.main_window_presenter.load_panel(self.add_edit_view)

    def save_department(self, dept_name, dept_id):
        department = Department(dept_id, dept_name)
        
        if self.model.get(department.id):
            self.model.update(department)
        else:
            self.model.add(department)
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)

    def delete_department(self, department):
        self.model.delete(department)
        self.load_data()

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