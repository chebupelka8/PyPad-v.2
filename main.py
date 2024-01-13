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
        self.setObjectName("main-widget")

        # Init layouts
        self.mainLayout = QVBoxLayout()
        self.workbenchLayout = QHBoxLayout()

        self.init_ui()
        self.setup_ui()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_O:
            self.fileTree.open_directory(FileDialog.get_open_directory())
        elif event.key() == Qt.Key.Key_P:
            self.fileTree.open_file(FileDialog.get_open_file_name())
        else:
            super().keyPressEvent(event)

    def init_ui(self) -> None:
        self.fileTree = FileTree()
        self.tabEditor = TabEditor()

        self.workbenchLayout.addWidget(self.fileTree, stretch=2)
        self.workbenchLayout.addWidget(self.tabEditor, stretch=5)

    def setup_ui(self) -> None:
        self.tabEditor.addTab(WelcomeScreen(), "Welcome")
        self.tabEditor.addTab(PythonCodeEditorArea("scr/widgets/file_tree.py"), "main.py")
        self.tabEditor.addTab(JsonCodeEditorArea("scr/data/theme.json"), "data.json")
        self.tabEditor.addTab(TextEditorArea("dist/data_font.txt"), "text.txt")
        self.tabEditor.addTab(ImageViewer("test_assets/java_game.png"), "image.png")

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
