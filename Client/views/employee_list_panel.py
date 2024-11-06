from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem

class EmployeeListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employees")
        
        layout = QVBoxLayout(self)
        
        self.employee_list = QListWidget()
        layout.addWidget(self.employee_list)
        
        self.add_button = QPushButton("Add Employee")
        layout.addWidget(self.add_button)
        
        self.add_button.clicked.connect(self.on_add_clicked)
        
    def set_presenter(self, presenter):
        self.presenter = presenter

    def add_item(self, employee):
        item = QListWidgetItem(f"{employee.name} - {employee.position}")
        self.employee_list.addItem(item)

    def on_add_clicked(self):
        self.presenter.open_add_edit_view()
