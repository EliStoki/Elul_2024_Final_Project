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
from presenters.department_presenter import DepartmentPresenter


class DepartmentEditPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Department")

        self.edited_department = None

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)  # Set margins for the main layout

        # Add a spacer at the top
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Header label in the center
        self.header_label = QLabel("Edit Department")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(self.header_label)

        # Add another spacer below the header
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Input fields with labels
        form_container = QVBoxLayout()
        form_container.setContentsMargins(40, 0, 40, 0)  # Add extra margins to the sides

        form_layout = QFormLayout()

        self.dept_id_label = QLabel("Department ID:")
        self.dept_id_input = QLineEdit()
        self.dept_id_input.setPlaceholderText("Enter department ID")
        form_layout.addRow(self.dept_id_label, self.dept_id_input)

        self.dept_name_label = QLabel("Department Name:")
        self.dept_name_input = QLineEdit()
        self.dept_name_input.setPlaceholderText("Enter department name")
        form_layout.addRow(self.dept_name_label, self.dept_name_input)

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

    def set_presenter(self, presenter : DepartmentPresenter):
        self.presenter = presenter

    def set_department(self, department):
        self.edited_department = department
        self.dept_id_input.setText(str(department.id))
        self.dept_name_input.set
    
    def on_save_clicked(self):
        dept_id = self.dept_id_input.text()
        dept_name = self.dept_name_input.text()
        self.presenter.update_department(dept_id, dept_name)
