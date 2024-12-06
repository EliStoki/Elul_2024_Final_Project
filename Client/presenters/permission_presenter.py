from models.permission import Permission
from presenters.main_window_presenter import MainWindowPresenter
from models.permission_da import PermissionDA

class PermissionPresenter:
    def __init__(self, model : PermissionDA, list_view, add_view, edit_view, main_window_presenter : MainWindowPresenter):
        self.model = model
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
        self.main_window_presenter.set_status_bar_text("Loading permissions...")
        self.list_view.clear()
        for permission in self.model.get_all():
            self.list_view.add_item(permission)
        self.main_window_presenter.set_status_bar_text("Permissions loaded successfully.")

    def open_add_view(self):
        self.add_view.floor_level_input.clear()
        self.add_view.building_input.clear()
        self.main_window_presenter.load_panel(self.add_view)

    def open_edit_view(self, permission: Permission):
        self.edit_view.editet_permission = permission.id
        self.edit_view.floor_level_input.setText(str(permission.floorLevel))
        self.edit_view.building_input.setText(permission.building)
        self.main_window_presenter.load_panel(self.edit_view)


    def add_permission(self, id, floor_level, building):
        permission = Permission(id=id, floorLevel=floor_level, building=building)
        response = self.model.add(permission)
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)
        self.main_window_presenter.set_status_bar_text(f"Permission {response} added successfully.")

    def update_permission(self, id, floor_level, building):
        permission = Permission(id=id, floorLevel=floor_level, building=building)
        self.model.update(permission)
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)
        self.main_window_presenter.set_status_bar_text(f"Permission {id} updated successfully.")

    def delete_permission(self, permission):
        if self.model.delete(permission):
            self.load_data()
            self.main_window_presenter.set_status_bar_text(f"Permission {permission.id} deleted successfully.")
        else:
            self.main_window_presenter.set_status_bar_text(f"Permission {permission.id} is in use and cannot be deleted.")

    def open_list_view(self):
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