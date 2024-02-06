from scr.scripts import FileLoader, restart_application

from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt


class _Dialog(QDialog):
    def __init__(self, __message: str, accept_title: str = "Ok", reject_title: str = "Cancel") -> None:
        super().__init__(f=Qt.WindowType.FramelessWindowHint)

        self.setWindowTitle("PyPad")
        self.setStyleSheet(FileLoader.load_style("scr/styles/dialog.css"))

        self.mainLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.mainLayout.addWidget(
            QLabel(__message), alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.mainLayout.addLayout(self.buttonLayout)

        self.acceptBtn = QPushButton(accept_title)
        self.acceptBtn.setObjectName("accept-btn")
        self.rejectBtn = QPushButton(reject_title)
        self.rejectBtn.setObjectName("reject-btn")

        self.acceptBtn.clicked.connect(self.accept)
        self.rejectBtn.clicked.connect(self.reject)

        self.buttonLayout.addWidget(self.acceptBtn, alignment=Qt.AlignmentFlag.AlignRight)
        self.buttonLayout.addWidget(self.rejectBtn, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.mainLayout)


class Restarter(_Dialog):
    def __init__(self) -> None:
        super().__init__("Do you want to restart the IDE to save the changes", "Restart")

        self.setMinimumWidth(500)

    def accept(self):
        restart_application()
