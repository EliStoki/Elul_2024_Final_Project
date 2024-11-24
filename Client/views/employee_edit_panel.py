from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QFormLayout,
    QSpacerItem,
    QSizePolicy,
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox


class EmployeeEditPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Employee")

        self.edited_employee = None

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)  # Set margins for the main layout

        # Add a spacer at the top
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Header label in the center
        self.header_label = QLabel("Edit Employee")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(self.header_label)

        # Add another spacer below the header
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Input fields with labels
        form_container = QVBoxLayout()
        form_container.setContentsMargins(150, 0, 150, 0)  # Add extra margins to the sides

        form_layout = QFormLayout()

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter name")
        form_layout.addRow(self.name_label, self.name_input)

        self.position_label = QLabel("Position:")
        self.position_input = QLineEdit()
        self.position_input.setPlaceholderText("Enter position")
        form_layout.addRow(self.position_label, self.position_input)

        self.department_label = QLabel("Department:")
        self.department_input = QComboBox()
        form_layout.addRow(self.department_label, self.department_input)

        self.permission_label = QLabel("Permission ID:")
        self.permission_input = QComboBox()
        form_layout.addRow(self.permission_label, self.permission_input)

        form_container.addLayout(form_layout)
        form_container.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(form_container)

        # Add another spacer below the form
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Buttons layout
        button_container = QHBoxLayout()
        button_container.setContentsMargins(40, 0, 40, 0)  # Add extra margins to the sides
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        button_container.addWidget(self.save_button)
        button_container.addWidget(self.cancel_button)
        main_layout.addLayout(button_container)

        # Add a spacer at the bottom
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Connect buttons to their respective methods
        self.save_button.clicked.connect(self.on_save_clicked)
        self.cancel_button.clicked.connect(lambda: self.presenter.open_list_view())

    def set_presenter(self, presenter):
        self.presenter = presenter

    def set_employee(self, employee):
        """
        Set the details of the employee to be edited.
        """
        self.edited_employee = employee
        self.name_input.setText(employee.name)
        self.position_input.setText(employee.position)
        self.department_input.setText(employee.department)

    def on_save_clicked(self):
        """
        Collect the updated data and notify the presenter.
        """
        if not self.edited_employee:
            return

        name = self.name_input.text()
        position = self.position_input.text()
        department = self.department_input.currentData()
        permission = self.permission_input.currentData()

        self.presenter.update_employee(self.edited_employee, name, position, department, permission)