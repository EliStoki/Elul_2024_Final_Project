from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QLineEdit,
    QComboBox,
)
from PySide6.QtGui import QIcon
from presenters.department_presenter import DepartmentPresenter
from models.department import Department


class DepartmentListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Departments")

        # Main layout with margins
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Top layout
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(10, 5, 10, 5)

        # Search bar layout
        search_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        # Add label "Filter By:"
        filter_label = QLabel("Filter By:")
        search_layout.addWidget(filter_label)

        # Create the filter dropdown
        self.filter_dropdown = QComboBox(self)
        self.filter_dropdown.addItems(["Department ID", "Name"])  # Filter options
        self.filter_dropdown.setCurrentIndex(1)  # Default to "Name"
        self.filter_dropdown.setFixedHeight(30)
        self.filter_dropdown.currentIndexChanged.connect(lambda: self.presenter.filter_table())
        search_layout.addWidget(self.filter_dropdown)

        # Create the search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setFixedHeight(30)
        self.search_bar.textChanged.connect(lambda: self.presenter.filter_table())
        search_layout.addWidget(self.search_bar)

        # Add button to add departments
        self.add_button = QPushButton("Add Department")
        self.add_button.setFixedHeight(30)
        button_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(lambda: self.presenter.open_add_view())

        # button to refresh the table
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setFixedHeight(30)  # Set button size
        button_layout.addWidget(self.refresh_button)
        self.refresh_button.clicked.connect(lambda: self.presenter.load_data())  # Refresh the table

        # Add layouts to the top layout
        top_layout.addLayout(search_layout)
        top_layout.addLayout(button_layout)

        # Add the top layout to the main layout
        main_layout.addLayout(top_layout)

        # Create the QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Department ID", "Name", "Actions"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)  # Disable editing
        # remove the row numbers
        self.table.verticalHeader().setVisible(False)

        main_layout.addWidget(self.table)

    def set_presenter(self, presenter : DepartmentPresenter):
        self.presenter = presenter

    def clear(self):
        self.table.setRowCount(0)

    def add_item(self, department : Department):
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
        edit_button.setIconSize(edit_button.sizeHint() * 0.8)
        edit_button.setFixedSize(30, 30)  # Set fixed size to fit the cell

        delete_button = QPushButton()
        delete_button.setIcon(QIcon("resources/delete icon.png"))
        delete_button.setIconSize(delete_button.sizeHint() * 0.8)
        delete_button.setFixedSize(30, 30)  # Set fixed size to fit the cell
        
        # Connect the buttons to the presenter
        edit_button.clicked.connect(lambda: self.presenter.open_edit_view(department))
        delete_button.clicked.connect(lambda: self.presenter.delete_department(department))

        # Add the buttons to the layout
        action_layout.addWidget(edit_button)
        action_layout.addWidget(delete_button)

        # Create a widget to hold the buttons and set it as the item for the 'Actions' column
        action_widget = QWidget()
        action_widget.setLayout(action_layout)
        self.table.setCellWidget(row_position, 2, action_widget)  # 2 is the 'Actions' column index
