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

class PermissionEditPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Permission")

        self.editet_permission = None

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)  # Set margins for the main layout

        # Add a spacer at the top
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Header label in the center
        self.header_label = QLabel("Edit Permission")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(self.header_label)

        # Add another spacer below the header
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Input fields with labels
        form_container = QVBoxLayout()
        form_container.setContentsMargins(40, 0, 40, 0)  # Add extra margins to the sides

        form_layout = QFormLayout()

        self.floor_level_label = QLabel("Floor Level:")
        self.floor_level_input = QLineEdit()
        self.floor_level_input.setPlaceholderText("Enter floor level")
        form_layout.addRow(self.floor_level_label, self.floor_level_input)

        self.building_label = QLabel("Building:")
        self.building_input = QLineEdit()
        self.building_input.setPlaceholderText("Enter building name")
        form_layout.addRow(self.building_label, self.building_input)

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

    def on_save_clicked(self):
        id = self.editet_permission
        floor_level = self.floor_level_input.text()
        building = self.building_input.text()
        self.presenter.update_permission(id, floor_level, building)
