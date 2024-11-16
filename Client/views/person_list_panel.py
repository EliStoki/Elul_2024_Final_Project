from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout
from PySide6.QtGui import QIcon

class PersonListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persons")

        # Main layout
        main_layout = QVBoxLayout(self)

        # Create the QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Age", "Address", "Actions"])  # Set column headers

        # Disable editing of table cells
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        main_layout.addWidget(self.table)

        # Add button to add persons
        self.add_button = QPushButton("Add Person")
        main_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(lambda: self.presenter.open_add_view())  # Open Add View

    def set_presenter(self, presenter):
        """Set the presenter for this view."""
        self.presenter = presenter

    def clear(self):
        """Clear the table."""
        self.table.setRowCount(0)

    def add_item(self, person):
        """Add a person to the table."""
        # Add a new row to the table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Set the row height
        self.table.setRowHeight(row_position, 40)

        # Insert each attribute into its respective column
        self.table.setItem(row_position, 0, QTableWidgetItem(str(person.id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(person.name))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(person.age)))
        self.table.setItem(row_position, 3, QTableWidgetItem(person.address))

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

        # Connect the buttons to the presenter
        # For edit, use the open_edit_view method
        edit_button.clicked.connect(lambda: self.presenter.open_edit_view(person))
        # For delete, use the delete_person method
        delete_button.clicked.connect(lambda: self.presenter.delete_person(person))

        # Add the buttons to the layout
        action_layout.addWidget(edit_button)
        action_layout.addWidget(delete_button)

        # Create a widget to hold the buttons and set it as the item for the 'Actions' column
        action_widget = QWidget()
        action_widget.setLayout(action_layout)
        self.table.setCellWidget(row_position, 4, action_widget)  # 4 is the 'Actions' column index
