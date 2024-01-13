from scr.scripts import FileLoader
from scr.data import IconPaths
from .welcome_screen import WelcomeScreen

from PySide6.QtWidgets import QTabWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


class TabEditor(QTabWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/tab_editor.css"))
        self.setObjectName("tab-editor")

        self.setTabsClosable(True)
        self.setIconSize(QSize(25, 25))
        self.tabCloseRequested.connect(self.removeTab)

    def removeTab(self, __index):
        super().removeTab(__index)

        if self.count() == 0:
            self.addTab(WelcomeScreen(), "Welcome!", IconPaths.MAIN)

    def addTab(self, widget, arg__2, icon=None):
        super().addTab(widget, arg__2)

        if icon != None:
            self.setTabIcon(self.indexOf(widget), QIcon(icon))


