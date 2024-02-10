from scr.scripts import FileLoader, restart_application

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit,
    QListWidget
)
from PySide6.QtCore import Qt


class _Dialog(QDialog):
    def __init__(self, __parent, __message: str, accept_title: str = "Ok", reject_title: str = "Cancel") -> None:
        super().__init__(__parent, f=Qt.WindowType.FramelessWindowHint)

        self.setStyleSheet(FileLoader.load_style("scr/styles/ui.css"))

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


class _InputDialog(QDialog):
    def __init__(
            self, __parent,
            __message: str,
            pasted_text: str = "", place_holder_text: str = "",
            accept_title: str = "Ok", reject_title: str = "Cancel"
    ) -> None:
        super().__init__(__parent, f=Qt.WindowType.FramelessWindowHint)

        self.setStyleSheet(FileLoader.load_style("scr/styles/ui.css"))

        self.mainLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.mainLayout.addWidget(
            QLabel(__message), alignment=Qt.AlignmentFlag.AlignCenter
        )

        # input line
        self.inputLine = QLineEdit()
        self.inputLine.setText(pasted_text)
        self.inputLine.setPlaceholderText(place_holder_text)
        self.mainLayout.addWidget(self.inputLine)

        # buttons
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


class _ListChanger(QListWidget):
    def __init__(self, __parent, *__values) -> None:
        super().__init__(__parent)

        self.setStyleSheet(FileLoader.load_style("scr/styles/ui.css"))
        self.addItems([*__values])


class Restarter(_Dialog):
    def __init__(self, __parent) -> None:
        super().__init__(__parent, "Do you want to restart the IDE to save the changes", "Restart")

        self.setMinimumWidth(500)

    def accept(self):
        restart_application()
