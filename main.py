from scr import (
    FileDialog, FileTree, TabEditor, SideBar,
    SettingsActionMenu, IconPaths, WelcomeScreen,
    FileChecker, FileLoader, PythonCodeEditorArea,
    HtmlCodeEditorArea, StyleCodeEditorArea, JsonCodeEditorArea,
    ImageViewer, TextEditorArea, WINDOW_SIZE, Restarter
)

import os
import sys

from PySide6.QtWidgets import (
    QWidget, QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout
)
from PySide6.QtCore import QModelIndex, Qt
from PySide6.QtGui import QIcon


class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

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
        self.sideBar = SideBar()
        self.settingActionMenu = SettingsActionMenu()
        self.restarter = Restarter(self)

        self.workbenchLayout.addWidget(self.sideBar, stretch=1)
        self.workbenchLayout.addWidget(self.fileTree, stretch=2)
        self.workbenchLayout.addWidget(self.tabEditor, stretch=7)

    def setup_ui(self) -> None:
        self.tabEditor.addTab(WelcomeScreen(), "Welcome!", IconPaths.SystemIcons.WELCOME)

        self.fileTree.clicked.connect(self.__click_file_tree)

        self.sideBar.settings_opener_connect(self.settingActionMenu.show)
        self.sideBar.file_tree_opener_connect(self.fileTree.show_hide_file_tree)

        self.settingActionMenu.connect_by_title("Themes...", self._theme_changer_test)

        self.mainLayout.addLayout(self.workbenchLayout)
        self.setLayout(self.mainLayout)

    def __click_file_tree(self, __index: QModelIndex) -> None:
        path = self.fileTree.get_path_by_index(__index)

        if os.path.isfile(path):
            self.__open_file_for_edit(path, self.fileTree.get_file_icon(__index))

    def __open_file_for_edit(self, __path: str, __icon) -> None:

        if FileChecker.is_python_file(__path):
            self.tabEditor.addTab(
                PythonCodeEditorArea(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_style_file(__path):
            self.tabEditor.addTab(
                StyleCodeEditorArea(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_json_file(__path):
            self.tabEditor.addTab(
                JsonCodeEditorArea(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_picture_file(__path):
            self.tabEditor.addTab(
                ImageViewer(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_html_file(__path):
            self.tabEditor.addTab(
                HtmlCodeEditorArea(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_readable(__path):
            try:
                self.tabEditor.addTab(
                    TextEditorArea(__path), os.path.basename(__path), __icon
                )
            except UnicodeDecodeError:
                pass

        self.tabEditor.setCurrentWidget(self.tabEditor.find_by_path(__path))

    def _theme_changer_test(self):
        from random import choice
        import json

        themes = [f"scr/data/themes/{i}" for i in os.listdir("scr/data/themes")]

        t = FileLoader.load_json("scr/data/settings.json")

        t["theme"]["path"] = choice(themes)

        with open("scr/data/settings.json", "w") as file:
            json.dump(t, file, indent=4)

        self.restarter.show()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(*WINDOW_SIZE)
        self.setWindowTitle("PyPad")
        self.setWindowIcon(QIcon("assets/icons/system_icons/window_icon.png"))
        self.setStyleSheet(FileLoader.load_style("scr/styles/main.css"))
        self.setObjectName("window")

        self.mainWidget = MainWidget()

        self.setCentralWidget(self.mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
