from PySide6.QtWidgets import QListWidget
from PySide6.QtCore import Qt

from scr.scripts import FileLoader


class Completer(QListWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.setStyleSheet(FileLoader.load_style("scr/styles/completer.css"))

    def set_items(self, __items: list[str]) -> None:
        self.clear()
        self.addItems(__items)
