from PySide6.QtWidgets import QWidget

class MainWindowPresenter:
    def __init__(self, main_view):
        self.main_view = main_view
        self.main_view.set_presenter(self)

    def add_panel(self, panel : QWidget):
        self.main_view.main_area.addWidget(panel)

    # loads panel according to the selected item in the sidebar
    def load_selected_panel(self, selected_panel):
        """
        Loads the panel corresponding to the selected model in the sidebar.
        :param current: Currently selected QListWidgetItem
        """
        index = self.main_view.sidebar.row(selected_panel)
        self.main_view.main_area.setCurrentIndex(index)

    # loads panel to the main area
    def load_panel(self, panel : QWidget):
        """
        Loads the specified panel.
        :param panel: Panel to load
        """
        # loads the new panel
        self.main_view.main_area.setCurrentWidget(panel)

    def set_status_bar_text(self, text):
        self.main_view.status_bar.setText(text)

    def run(self):
        self.main_view.show()        