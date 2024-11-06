from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

class PersonAddEditPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add/Edit Person")
        
        layout = QVBoxLayout(self)
        
        # Input fields for person details
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        layout.addWidget(self.name_input)
        
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")
        layout.addWidget(self.age_input)
        
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Address")
        layout.addWidget(self.address_input)
        
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)
        
        self.save_button.clicked.connect(self.on_save_clicked)
        
    def set_presenter(self, presenter):
        self.presenter = presenter
    
    def on_save_clicked(self):
        name = self.name_input.text()
        age = self.age_input.text()
        address = self.address_input.text()
        self.presenter.save_person(name, age, address)
