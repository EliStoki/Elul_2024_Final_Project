import sys
from PySide6.QtWidgets import QApplication
from model import EmployeeModel
from view import EmployeeView
from controller import EmployeeController

def main():
    app = QApplication(sys.argv)

    # Instantiate model, view, and controller
    model = EmployeeModel()
    view = EmployeeView()
    controller = EmployeeController(model, view)

    # Show the view
    view.setWindowTitle("Employee Profile Management System")
    view.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
