from PySide6.QtWidgets import QMainWindow, QListWidget, QStackedWidget, QVBoxLayout, QWidget, QListWidgetItem

# Main application window managing different model panels.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Management System")
        
        # Sidebar list to navigate between models.
        self.sidebar = QListWidget()
        self.sidebar.addItem("Persons")
        self.sidebar.addItem("Employees")
        self.sidebar.addItem("Departments")
        self.sidebar.addItem("Permissions")
        
        # Main area where model-specific panels are displayed.
        self.main_area = QStackedWidget()
        
        # Set up layout for the main window.
        layout = QVBoxLayout()
        layout.addWidget(self.sidebar)
        layout.addWidget(self.main_area)
        
        # Central widget containing sidebar and main area.
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Connect selection change in sidebar to a method to switch views.
        self.sidebar.currentItemChanged.connect(self.load_selected_panel)
        
    def load_selected_panel(self, current, previous):
        """
        Loads the panel corresponding to the selected model in the sidebar.
        :param current: Currently selected QListWidgetItem
        :param previous: Previously selected QListWidgetItem
        """
        index = self.sidebar.row(current)
        self.main_area.setCurrentIndex(index)
