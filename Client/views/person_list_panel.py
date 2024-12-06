from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
    QComboBox,
    QLabel,
)
from PySide6.QtGui import QIcon


class PersonListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persons")

        # Main layout with margins
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)  # Set margin for the layout (left, top, right, bottom)

        # Top layout
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(10, 5, 10, 5)  # Set margin for the layout (left, top, right, bottom)

        # Search bar layout
        search_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        # Add label "Filter By:"
        filter_label = QLabel("Filter By:")
        #filter_label.setFixedSize(70,30) # Set label size
        search_layout.addWidget(filter_label)

        # Create the filter dropdown
        self.filter_dropdown = QComboBox(self)
        self.filter_dropdown.addItems(["ID", "Name", "Age", "Address"])  # Filter options
        self.filter_dropdown.setCurrentIndex(1)  # Default to "Name"
        self.filter_dropdown.setFixedHeight(30)  # Set dropdown size
        self.filter_dropdown.currentIndexChanged.connect(lambda: self.presenter.filter_table())  # Re-filter on column change
        search_layout.addWidget(self.filter_dropdown)

        # Create the search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setFixedHeight(30)   # Set search bar size
        self.search_bar.textChanged.connect(lambda: self.presenter.filter_table())  # Filter on text change
        search_layout.addWidget(self.search_bar)

        # Add button to add persons
        self.add_button = QPushButton("Add Person")
        self.add_button.setFixedHeight(30)  # Set button size
        button_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(lambda: self.presenter.open_add_view())  # Open Add View

        # button to refresh the table
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setFixedHeight(30)  # Set button size
        button_layout.addWidget(self.refresh_button)
        self.refresh_button.clicked.connect(lambda: self.presenter.load_data())  # Refresh the table

        top_layout.addLayout(search_layout)
        top_layout.addLayout(button_layout)

        # Add the search layout to the main layout
        main_layout.addLayout(top_layout)

        # Create the QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Age", "Address", "Actions"])  # Set column headers
        self.table.setColumnWidth(4, 100)  # Set column width for 'Actions'
        # remove the row numbers
        self.table.verticalHeader().setVisible(False)
        
        # Disable editing of table cells
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        main_layout.addWidget(self.table)

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
        edit_button.setIconSize(edit_button.sizeHint() * 0.8)
        edit_button.setFixedSize(30, 30)  # Set fixed size to fit the cell

        delete_button = QPushButton()
        delete_button.setIcon(QIcon("resources/delete icon.png"))
        delete_button.setIconSize(delete_button.sizeHint() * 0.8)
        delete_button.setFixedSize(30, 30)  # Set fixed size to fit the cell

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
