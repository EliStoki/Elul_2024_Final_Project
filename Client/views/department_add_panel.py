from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

class DepartmentAddPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add/Edit Department")
        
        # Layout setup
        layout = QVBoxLayout(self)
        
        # Input fields for department name and ID
        self.dept_name_input = QLineEdit()
        self.dept_name_input.setPlaceholderText("Department Name")
        layout.addWidget(self.dept_name_input)
        
        self.dept_id_input = QLineEdit()
        self.dept_id_input.setPlaceholderText("Department ID")
        layout.addWidget(self.dept_id_input)
        
        # Save button
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)
        
        # Connect button to save method
        self.save_button.clicked.connect(self.on_save_clicked)
        
    def set_presenter(self, presenter):
        self.presenter = presenter
    
    def on_save_clicked(self):
        dept_name = self.dept_name_input.text()
        dept_id = self.dept_id_input.text()
        self.presenter.save_department(dept_name, dept_id)
