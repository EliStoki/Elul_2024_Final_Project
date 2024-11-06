from models.department import Department

class DepartmentPresenter:
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
        self.list_view.department_list.clear()
        for department in self.model:
            self.list_view.add_item(department)

    def open_add_edit_view(self, department=None):
        if department:
            self.add_edit_view.dept_name_input.setText(department.dept_name)
            self.add_edit_view.dept_id_input.setText(department.dept_id)
        else:
            self.add_edit_view.dept_name_input.clear()
            self.add_edit_view.dept_id_input.clear()
        self.add_edit_view.show()

    def save_department(self, dept_name, dept_id):
        department = Department(dept_name, dept_id)
        self.model.append(department)
        self.load_data()
        self.add_edit_view.hide()

    def delete_department(self, department):
        self.model.remove(department)
        self.load_data()
