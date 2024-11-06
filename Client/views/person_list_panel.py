from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem

class PersonListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persons")
        
        layout = QVBoxLayout(self)
        
        self.person_list = QListWidget()
        layout.addWidget(self.person_list)
        
        self.add_button = QPushButton("Add Person")
        layout.addWidget(self.add_button)
        
        self.add_button.clicked.connect(self.on_add_clicked)
        
    def set_presenter(self, presenter):
        self.presenter = presenter

    def add_item(self, person):
        item = QListWidgetItem(f"{person.name} - Age: {person.age}")
        self.person_list.addItem(item)

    def on_add_clicked(self):
        self.presenter.open_add_edit_view()
