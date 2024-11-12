from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel

class Person:
    def __init__(self, person_id, name, age, address):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.address = address

class PersonListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persons")

        # Main layout
        main_layout = QVBoxLayout(self)

        # Create the QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)  # We have 4 columns: ID, Name, Age, Address
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Age", "Address"])  # Set column headers

        # Disable editing of table cells
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        main_layout.addWidget(self.table)

        # Add button to add persons
        self.add_button = QPushButton("Add Person")
        main_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.on_add_clicked)

    def set_presenter(self, presenter):
        self.presenter = presenter

    def clear(self):
        self.table.setRowCount(0)
    
    def add_item(self, person):
        # Add a new row to the table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Insert each attribute into its respective column
        self.table.setItem(row_position, 0, QTableWidgetItem(str(person.person_id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(person.name))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(person.age)))
        self.table.setItem(row_position, 3, QTableWidgetItem(person.address))

    def on_add_clicked(self):
        self.presenter.open_add_edit_view()
