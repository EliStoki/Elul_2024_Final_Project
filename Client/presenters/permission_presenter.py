from models.permission import Permission
from presenters.main_window_presenter import MainWindowPresenter
from models.permission_da import PermissionDA

class PermissionPresenter:
    def __init__(self, model : PermissionDA, list_view, add_edit_view, main_window_presenter : MainWindowPresenter):
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
        for permission in self.model.get_all():
            self.list_view.add_item(permission)

    def open_add_edit_view(self, permission=None):
        if permission:
            self.add_edit_view.floor_level_input.setText(str(permission.floorLevel))
            self.add_edit_view.building_input.setText(permission.building)
        else:
            self.add_edit_view.floor_level_input.clear()
            self.add_edit_view.building_input.clear()

        self.main_window_presenter.load_panel(self.add_edit_view)

    def save_permission(self, id, floor_level, building):
        permission = Permission(id=id, floorLevel=floor_level, building=building)
        
        if self.model.get(permission.id):
            self.model.update(permission)
        else:
            self.model.add(permission)
        self.load_data()
        self.main_window_presenter.load_panel(self.list_view)

    def delete_permission(self, permission):
        self.model.delete(permission)
        self.load_data()
