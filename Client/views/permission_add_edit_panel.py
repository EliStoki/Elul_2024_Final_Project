from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

class PermissionAddEditPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add/Edit Permission")
        
        layout = QVBoxLayout(self)
        
        # Input fields for permission details
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Permission ID")
        layout.addWidget(self.id_input)

        self.floor_level_input = QLineEdit()
        self.floor_level_input.setPlaceholderText("Floor Level")
        layout.addWidget(self.floor_level_input)
        
        self.building_input = QLineEdit()
        self.building_input.setPlaceholderText("Building")
        layout.addWidget(self.building_input)
        
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)
        
        self.save_button.clicked.connect(self.on_save_clicked)
        
    def set_presenter(self, presenter):
        self.presenter = presenter
    
    def on_save_clicked(self):
        id = self.id_input.text()
        floor_level = self.floor_level_input.text()
        building = self.building_input.text()
        self.presenter.save_permission(id, floor_level, building)
