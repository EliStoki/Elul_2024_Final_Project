from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QHBoxLayout
from PySide6.QtGui import QIcon, QPixmap
from models.employee import Employee
from models.permission import Permission
from models.department import Department
from presenters.employee_presenter import EmployeePresenter

class EmployeeListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employees")

        # Main layout
        main_layout = QVBoxLayout(self)

        # Create the QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Position", "Department", "Image", "Permissions", "Actions"])  # Set column headers

        # Disable editing of table cells
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        main_layout.addWidget(self.table)

        # Add button to add employees
        self.add_button = QPushButton("Add Employee")
        main_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(lambda: self.presenter.open_add_edit_view())

    def set_presenter(self, presenter: EmployeePresenter):
        self.presenter = presenter

    def clear(self):
        self.table.setRowCount(0)

    def add_item(self, employee: Employee):
        # Add a new row to the table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        
        # Set the row height
        self.table.setRowHeight(row_position, 60)

        # Insert each attribute into its respective column
        self.table.setItem(row_position, 0, QTableWidgetItem(str(employee.employee_id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(employee.name))
        self.table.setItem(row_position, 2, QTableWidgetItem(employee.position))
        self.table.setItem(row_position, 3, QTableWidgetItem(employee.department.deptName))
        
        # Display employee image
        image_label = QLabel()
        pixmap = QPixmap(employee.image_url)
        image_label.setPixmap(pixmap.scaled(50, 50))  # Scale the image for consistent row height
        self.table.setCellWidget(row_position, 4, image_label)

        # Display permissions
        self.table.setItem(row_position, 5, QTableWidgetItem(employee.permission.id))

        # Create action buttons for each row
        action_layout = QHBoxLayout()
        edit_button = QPushButton()
        edit_button.setIcon(QIcon("resources/edit icon.png"))
        edit_button.setIconSize(edit_button.sizeHint())
        edit_button.setFixedSize(edit_button.sizeHint())

        delete_button = QPushButton()
        delete_button.setIcon(QIcon("resources/delete icon.png"))
        delete_button.setIconSize(delete_button.sizeHint())
        delete_button.setFixedSize(delete_button.sizeHint())

        # Connect the buttons to the presenter (Pass row index and employee_id as data)
        edit_button.clicked.connect(lambda: self.presenter.open_add_edit_view(employee))
        delete_button.clicked.connect(lambda: self.presenter.delete_employee(employee))

        # Add the buttons to the layout
        action_layout.addWidget(edit_button)
        action_layout.addWidget(delete_button)

        # Create a widget to hold the buttons and set it as the item for the 'Actions' column
        action_widget = QWidget()
        action_widget.setLayout(action_layout)
        self.table.setCellWidget(row_position, 6, action_widget)  # 6 is the 'Actions' column index
