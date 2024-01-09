from scr.scripts import FileLoader

from PySide6.QtWidgets import QTabWidget


class TabEditor(QTabWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/tab_editor.css"))
        self.setObjectName("tab-editor")

        self.setTabsClosable(True)

