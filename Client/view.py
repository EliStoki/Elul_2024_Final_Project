from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget

class EmployeeView(QWidget):
    def __init__(self):
        super().__init__()
        
        # Widgets
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.department_label = QLabel("Department:")
        self.department_input = QLineEdit()
        self.role_label = QLabel("Role:")
        self.role_input = QLineEdit()
        self.photo_label = QLabel("Photo (URL):")
        self.photo_input = QLineEdit()

        # Buttons
        self.add_button = QPushButton("Add Employee")
        self.update_button = QPushButton("Update Employee")
        self.delete_button = QPushButton("Delete Employee")
        self.load_button = QPushButton("Load Employee")

        # Employee list
        self.employee_list = QListWidget()

        # Layout
        layout = QVBoxLayout()
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.name_label)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.department_label)
        form_layout.addWidget(self.department_input)
        form_layout.addWidget(self.role_label)
        form_layout.addWidget(self.role_input)
        form_layout.addWidget(self.photo_label)
        form_layout.addWidget(self.photo_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.load_button)

        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        layout.addWidget(QLabel("Employee List"))
        layout.addWidget(self.employee_list)

        self.setLayout(layout)

    def get_employee_details(self):
        name = self.name_input.text()
        department = self.department_input.text()
        role = self.role_input.text()
        photo = self.photo_input.text()
        return name, department, role, photo

    def set_employee_details(self, name, department, role, photo):
        self.name_input.setText(name)
        self.department_input.setText(department)
        self.role_input.setText(role)
        self.photo_input.setText(photo)

    def clear_inputs(self):
        self.name_input.clear()
        self.department_input.clear()
        self.role_input.clear()
        self.photo_input.clear()
