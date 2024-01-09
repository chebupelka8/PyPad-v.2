from scr.scripts import FileLoader

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Qt


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/welcome_screen.css"))
        self.setObjectName("welcome-screen")

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(QLabel("Welcome"), alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.mainLayout)
