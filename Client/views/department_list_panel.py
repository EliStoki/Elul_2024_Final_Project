from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem

class DepartmentListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Departments")
        
        # Layout setup
        layout = QVBoxLayout(self)
        
        # List widget to display departments
        self.department_list = QListWidget()
        layout.addWidget(self.department_list)
        
        # Button to add a new department
        self.add_button = QPushButton("Add Department")
        layout.addWidget(self.add_button)
        
        # Connect button to a method for adding
        self.add_button.clicked.connect(self.on_add_clicked)
        
    def set_presenter(self, presenter):
        """
        Connects to the presenter to handle button actions.
        """
        self.presenter = presenter

    def add_item(self, department):
        """
        Add a department item to the list.
        """
        item = QListWidgetItem(f"{department.dept_name} (ID: {department.dept_id})")
        self.department_list.addItem(item)

    def on_add_clicked(self):
        """
        Triggered when the add button is clicked.
        """
        self.presenter.open_add_edit_view()
