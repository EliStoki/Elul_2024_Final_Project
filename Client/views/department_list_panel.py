from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout
from PySide6.QtGui import QIcon

class DepartmentListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Departments")

        # Main layout
        main_layout = QVBoxLayout(self)

        # Create the QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Department ID", "Name", "Actions"])  # Set column headers

        # Disable editing of table cells
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        main_layout.addWidget(self.table)

        # Add button to add departments
        self.add_button = QPushButton("Add Department")
        main_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(lambda: self.presenter.open_add_edit_view())

    def set_presenter(self, presenter):
        self.presenter = presenter

    def clear(self):
        self.table.setRowCount(0)

    def add_item(self, department):
        # Add a new row to the table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        
        # Set the row height
        self.table.setRowHeight(row_position, 40)

        # Insert each attribute into its respective column
        self.table.setItem(row_position, 0, QTableWidgetItem(str(department.id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(department.deptName))

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

        # Connect the buttons to the presenter (Pass row index and department_id as data)
        edit_button.clicked.connect(lambda: self.presenter.open_add_edit_view(department))
        delete_button.clicked.connect(lambda: self.presenter.delete_department(department))

        # Add the buttons to the layout
        action_layout.addWidget(edit_button)
        action_layout.addWidget(delete_button)

        # Create a widget to hold the buttons and set it as the item for the 'Actions' column
        action_widget = QWidget()
        action_widget.setLayout(action_layout)
        self.table.setCellWidget(row_position, 2, action_widget)  # 2 is the 'Actions' column index
