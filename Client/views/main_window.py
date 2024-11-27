from PySide6.QtWidgets import QMainWindow, QListWidget, QStackedWidget, QHBoxLayout, QWidget, QVBoxLayout, QLabel
from presenters.main_window_presenter import MainWindowPresenter

# Main application window managing different model panels.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Management System")

        self.setMinimumHeight(650)
        self.setMinimumWidth(900)
        
        # Sidebar list to navigate between models.
        self.sidebar = QListWidget()
        self.sidebar.addItem("Employees")
        self.sidebar.addItem("Departments")
        self.sidebar.addItem("Permissions")
        self.sidebar.addItem("Persons")

        # set slide bar width
        self.sidebar.setMaximumWidth(150)
        self.sidebar.setContentsMargins(5,100,5,100)
        
        # the right side layout of the main window
        self.right_side_layout = QVBoxLayout()

        # A Status bar at the bottom of the window right layout
        self.status_bar = QLabel("Ready")
        self.status_bar.setContentsMargins(20, 10, 10, 10) 

        # Main area where model-specific panels are displayed.
        self.main_area = QStackedWidget()
        
        self.right_side_layout.addWidget(self.main_area)
        self.right_side_layout.addWidget(self.status_bar)

        # Set up layout for the main window.
        layout = QHBoxLayout()
        layout.addWidget(self.sidebar)
        
        layout.addLayout(self.right_side_layout)
        
        # Central widget containing sidebar and main area.
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Connect selection change in sidebar to a method to switch views.
        self.sidebar.currentItemChanged.connect(self.load_selected_panel)
        
    def set_presenter(self, presenter : MainWindowPresenter):
        self.presenter = presenter

    def load_selected_panel(self, current):
        self.presenter.load_selected_panel(current)
