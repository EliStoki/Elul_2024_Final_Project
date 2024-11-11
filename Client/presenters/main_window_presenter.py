class MainWindowPresenter:
    def __init__(self, main_view):
        self.main_view = main_view
        self.main_view.set_presenter(self)

    def add_panel(self, panel):
        self.main_view.main_area.addWidget(panel)

    def load_panel(self, selected_panel):
        """
        Loads the panel corresponding to the selected model in the sidebar.
        :param current: Currently selected QListWidgetItem
        """
        index = self.main_view.sidebar.row(selected_panel)
        self.main_view.main_area.setCurrentIndex(index)

    def run(self):
        self.main_view.show()        