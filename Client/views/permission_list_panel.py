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


class PermissionListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Permissions")

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
        search_layout.addWidget(filter_label)

        # Create the filter dropdown
        self.filter_dropdown = QComboBox(self)
        self.filter_dropdown.addItems(["Permission ID", "Building", "Floor Level"])  # Filter options
        self.filter_dropdown.setCurrentIndex(0)  # Default to "Permission ID"
        self.filter_dropdown.setFixedHeight(30)  # Set dropdown size
        self.filter_dropdown.currentIndexChanged.connect(lambda: self.presenter.filter_table())  # Re-filter on column change
        search_layout.addWidget(self.filter_dropdown)

        # Create the search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setFixedHeight(30)  # Set search bar size
        self.search_bar.textChanged.connect(lambda: self.presenter.filter_table())  # Filter on text change
        search_layout.addWidget(self.search_bar)

        # Add button to add permissions
        self.add_button = QPushButton("Add Permission")
        self.add_button.setFixedHeight(30)  # Set button size
        button_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(lambda: self.presenter.open_add_view())  # Open Add View

        top_layout.addLayout(search_layout)
        top_layout.addLayout(button_layout)

        # Add the top layout to the main layout
        main_layout.addLayout(top_layout)

        # Create the QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Permission ID", "Building", "Floor Level", "Actions"])  # Set column headers

        # Disable editing of table cells
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        main_layout.addWidget(self.table)

    def set_presenter(self, presenter):
        self.presenter = presenter

    def clear(self):
        self.table.setRowCount(0)

    def add_item(self, permission):
        # Add a new row to the table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Set the row height
        self.table.setRowHeight(row_position, 40)

        # Insert each attribute into its respective column
        self.table.setItem(row_position, 0, QTableWidgetItem(str(permission.id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(permission.building))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(permission.floorLevel)))

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
        edit_button.clicked.connect(lambda: self.presenter.open_edit_view(permission))
        delete_button.clicked.connect(lambda: self.presenter.delete_permission(permission))

        # Add the buttons to the layout
        action_layout.addWidget(edit_button)
        action_layout.addWidget(delete_button)

        # Create a widget to hold the buttons and set it as the item for the 'Actions' column
        action_widget = QWidget()
        action_widget.setLayout(action_layout)
        self.table.setCellWidget(row_position, 3, action_widget)  # 3 is the 'Actions' column index
