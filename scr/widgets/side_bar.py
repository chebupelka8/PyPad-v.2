from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap

from scr.scripts import FileLoader


class SideBarButton(QPushButton):
    def __init__(self, __path_to_icon: str) -> None:
        super().__init__()

        self.setFixedSize(30, 30)
        self.setIcon(QPixmap(__path_to_icon))
        self.setIconSize(self.iconSize() * 1.2)


class SideBar(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/side_bar.css"))
        self.setObjectName("side-bar")

        self.setMaximumWidth(50)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.menuAppsBtn = SideBarButton("assets/icons/system_icons/apps.png")
        self.mainLayout.addWidget(self.menuAppsBtn, Qt.AlignmentFlag.AlignHCenter)

        self.fileTreeOpenerBtn = SideBarButton("assets/icons/system_icons/folder-open.png")
        self.mainLayout.addWidget(self.fileTreeOpenerBtn, Qt.AlignmentFlag.AlignHCenter)

        self.openSettingsBtn = SideBarButton("assets/icons/system_icons/settings.png")
        self.mainLayout.addWidget(self.openSettingsBtn, Qt.AlignmentFlag.AlignHCenter)

        self.mainLayout.addItem(QSpacerItem(30, 2000, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum))

    def file_tree_opener_connect(self, __command) -> None:
        self.fileTreeOpenerBtn.clicked.connect(__command)
