from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

class EmployeeAddEditPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add/Edit Employee")
        
        layout = QVBoxLayout(self)
        
        # Input fields for employee details
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        layout.addWidget(self.name_input)
        
        self.position_input = QLineEdit()
        self.position_input.setPlaceholderText("Position")
        layout.addWidget(self.position_input)
        
        self.dept_input = QLineEdit()
        self.dept_input.setPlaceholderText("Department")
        layout.addWidget(self.dept_input)
        
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)
        
        self.save_button.clicked.connect(self.on_save_clicked)
        
    def set_presenter(self, presenter):
        self.presenter = presenter
    
    def on_save_clicked(self):
        name = self.name_input.text()
        position = self.position_input.text()
        dept = self.dept_input.text()
        self.presenter.save_employee(name, position, dept)
