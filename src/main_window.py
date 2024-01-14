from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Qt

from res.compiled.main import Ui_MainWindow
from src.cycle_parser import parse_cycle_file


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowStaysOnTopHint)

        self.cycles = []
        self.current_cycle = 0

        self.setupUi(self)

        self._connect_actions()
        self._connect_buttons()

    def update_cycle(self, index):
        self.cycle_name_label.setText(self.cycles[index])

    def _connect_actions(self):
        self.action_open.triggered.connect(self.__open_action_callback)

    def _connect_buttons(self):
        self.next_btn.released.connect(self.__next_btn_callback)
        self.previous_btn.released.connect(self.__prev_btn_callback)

    def __open_action_callback(self):
        filepath, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "Cycle files (*.cy)")
        self.cycles = parse_cycle_file(filepath)
        self.current_cycle = 0
        self.update_cycle(0)

    def __next_btn_callback(self):
        cycles_size = len(self.cycles)
        if len(self.cycles) <= 0:
            return

        self.current_cycle = (self.current_cycle + 1) % cycles_size
        self.update_cycle(self.current_cycle)

    def __prev_btn_callback(self):
        cycles_size = len(self.cycles)
        if len(self.cycles) <= 0:
            return

        self.current_cycle = (self.current_cycle - 1) % cycles_size
        self.update_cycle(self.current_cycle)

