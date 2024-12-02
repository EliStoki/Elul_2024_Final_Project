from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread
from presenters.update_worker import UpdateWorker

class MainWindowPresenter:
    def __init__(self, main_view):
        self.main_view = main_view
        self.main_view.set_presenter(self)
        self.main_view.sidebar.setCurrentRow(0)
        # self.run_update_worker()

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

    def run_update_worker(self):
        self.thread = QThread()
        self.update_worker = UpdateWorker(self.main_view.main_area)
        self.update_worker.moveToThread(self.thread)
        self.thread.started.connect(self.update_worker.run)
        self.update_worker.finished.connect(self.thread.quit)
        self.update_worker.progress.connect(self.update_panel)
        self.thread.start()

    def update_panel(self, n):
        self.main_view.main_area.widget(n).presenter.load_data()       

    def run(self):
        self.main_view.show()