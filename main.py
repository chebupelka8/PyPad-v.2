from scr import *

import sys
from PySide6.QtWidgets import (
    QWidget, QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout
)


class MainWidget(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        # Self
        self.setObjectName("main")

        # Init layouts
        self.mainLayout = QVBoxLayout()
        self.workbenchLayout = QHBoxLayout()

        self.init_ui()
        self.setup_ui()

    def init_ui(self) -> None:
        self.codeArea = CodeEditorArea()
        self.fileTree = FileTree()
        self.tabEditor = TabEditor()

        self.workbenchLayout.addWidget(self.fileTree, stretch=2)
        self.workbenchLayout.addWidget(self.tabEditor, stretch=5)

    def setup_ui(self) -> None:
        self.tabEditor.addTab(WelcomeScreen(), "Welcome")
        self.tabEditor.addTab(self.codeArea, "main.py")

        self.mainLayout.addLayout(self.workbenchLayout)
        self.setLayout(self.mainLayout)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(*WINDOW_SIZE)
        self.setWindowTitle("PyPad v2.0 alpha")
        self.setStyleSheet(FileLoader.load_style("scr/styles/main.css"))
        self.setObjectName("window")

        self.mainWidget = MainWidget(self)
        self.setCentralWidget(self.mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
