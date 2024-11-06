from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem

class PermissionListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Permissions")
        
        layout = QVBoxLayout(self)
        
        self.permission_list = QListWidget()
        layout.addWidget(self.permission_list)
        
        self.add_button = QPushButton("Add Permission")
        layout.addWidget(self.add_button)
        
        self.add_button.clicked.connect(self.on_add_clicked)
        
    def set_presenter(self, presenter):
        self.presenter = presenter

    def add_item(self, permission):
        item = QListWidgetItem(f"{permission.building} - Floor {permission.floor_level}")
        self.permission_list.addItem(item)

    def on_add_clicked(self):
        self.presenter.open_add_edit_view()
