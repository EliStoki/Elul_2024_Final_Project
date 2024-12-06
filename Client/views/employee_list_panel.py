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
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QMovie
from models.employee import Employee
from presenters.employee_presenter import EmployeePresenter

class EmployeeListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employees")

        # Main layout with margins
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

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
        self.filter_dropdown.addItems(["ID", "Name", "Position", "Department"])  # Filter options
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

        # Add button to add employees
        self.add_button = QPushButton("Add Employee")
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
        self.main_layout.addLayout(top_layout)

        # Create the QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["Image", "ID", "Name", "Position", "Department", "Permissions", "Actions"]
        )
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)  # Disable editing
        # remove the row numbers
        self.table.verticalHeader().setVisible(False)

        self.main_layout.addWidget(self.table)

        # Create the loading label (hidden by default)
        self.loading_label = QLabel(self)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setVisible(False)
        self.main_layout.addWidget(self.loading_label)

        # Set up the loading GIF
        self.loading_gif = QMovie("resources/Loading_Animation.gif")  # Replace with your loading GIF path
        self.loading_label.setMovie(self.loading_gif)
        self.loading_gif.start()

    def set_presenter(self, presenter: EmployeePresenter):
        self.presenter = presenter

    def clear(self):
        self.table.setRowCount(0)

    def add_item(self, employee: Employee, dept_name, url_content):
        # Add a new row to the table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Set the row height
        self.table.setRowHeight(row_position, 60)

        # Insert each attribute into its respective column
        self.table.setItem(row_position, 1, QTableWidgetItem(str(employee.id)))
        self.table.setItem(row_position, 2, QTableWidgetItem(employee.name))
        self.table.setItem(row_position, 3, QTableWidgetItem(employee.position))
        self.table.setItem(row_position, 4, QTableWidgetItem(dept_name))

        # Display employee image
        image_label = QLabel()

        if url_content:
            # Load the image into QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(url_content)

            # Set the pixmap to the QLabel
            image_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio))  # Scale the image for consistent row height
        else:
            image_label.setText("No Image")

        # Add the image label to the table
        self.table.setCellWidget(row_position, 0, image_label)

        # Display permissions
        self.table.setItem(row_position, 5, QTableWidgetItem(str(employee.permission_id)))

        # Create action buttons for each row
        action_layout = QHBoxLayout()

        delete_button = QPushButton()
        delete_button.setIcon(QIcon("resources/delete icon.png"))
        delete_button.setIconSize(delete_button.sizeHint() * 0.8)
        delete_button.setFixedSize(30, 30)  # Set fixed size to fit the cell

        # Connect the buttons to the presenter
        delete_button.clicked.connect(lambda: self.presenter.delete_employee(employee))

        # Add the buttons to the layout
        action_layout.addWidget(delete_button)

        # Create a widget to hold the buttons and set it as the item for the 'Actions' column
        action_widget = QWidget()
        action_widget.setLayout(action_layout)
        self.table.setCellWidget(row_position, 6, action_widget)  # 6 is the 'Actions' column index

    def loading(self, mode: bool):
        self.loading_label.setVisible(mode)
        self.loading_gif.start()
        self.table.setVisible(not mode)
