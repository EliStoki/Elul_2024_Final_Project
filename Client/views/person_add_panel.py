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
from presenters.person_presenter import PersonPresenter

class PersonAddPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Person")
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)  # Set margins for the main layout

        # Add a spacer at the top
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Header label in the center
        self.header_label = QLabel("Add Person")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(self.header_label)

        # Add another spacer below the header
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Input fields with labels
        form_container = QVBoxLayout()
        form_container.setContentsMargins(200, 0, 200, 0)  # Add extra margins to the sides

        form_layout = QFormLayout()

        self.id_label = QLabel("ID:")
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter person ID")
        form_layout.addRow(self.id_label, self.id_input)

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter name")
        form_layout.addRow(self.name_label, self.name_input)

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter age")
        form_layout.addRow(self.age_label, self.age_input)

        self.address_label = QLabel("Address:")
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter address")
        form_layout.addRow(self.address_label, self.address_input)

        form_container.addLayout(form_layout)
        form_container.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(form_container)

        # Add another spacer below the form
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Buttons layout
        button_container = QHBoxLayout()
        button_container.setContentsMargins(200, 0, 200, 0)  # Add extra margins to the sides
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

    def set_presenter(self, presenter : PersonPresenter):
        self.presenter = presenter

    def on_save_clicked(self):
        id = self.id_input.text()
        name = self.name_input.text()
        age = self.age_input.text()
        address = self.address_input.text()
        self.presenter.add_person(id, name, age, address)
