from PySide6.QtCore import QObject, Signal
import time

class UpdateWorker(QObject):
    finished = Signal()
    progress = Signal(int)

    def __init__(self, main_area):
        super().__init__()
        self.main_area = main_area

    def run(self):
        while True:
            time.sleep(30)
            for n in range(4):
                self.main_area.widget(n).presenter.load_data()