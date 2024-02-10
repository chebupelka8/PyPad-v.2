from scr.scripts import FileLoader, restart_application

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit,
    QListWidget
)
from PySide6.QtCore import Qt

import os


class _DialogWindow(QDialog):
    def __init__(self, __parent) -> None:
        super().__init__(__parent, f=Qt.WindowType.FramelessWindowHint)

        self.setStyleSheet(FileLoader.load_style("scr/styles/ui.css"))


class _Dialog(_DialogWindow):
    def __init__(self, __parent, __message: str, accept_title: str = "Ok", reject_title: str = "Cancel") -> None:
        super().__init__(__parent)

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


class _InputDialog(_DialogWindow):
    def __init__(
            self, __parent,
            __message: str,
            pasted_text: str = "", place_holder_text: str = "",
            accept_title: str = "Ok", reject_title: str = "Cancel"
    ) -> None:
        super().__init__(__parent)

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


class _ListChanger(_DialogWindow):
    def __init__(self, __parent, *__values, width: int = 200, height: int = 400) -> None:
        super().__init__(__parent)

        self.setMinimumSize(width, height)

        self.mainLayout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.addItems([*__values])
        self.mainLayout.addWidget(self.listWidget)

        self.setLayout(self.mainLayout)

    def show(self):
        self.listWidget.setFocus()
        super().show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

        elif event.key() == Qt.Key.Key_Return:
            self.close()

        else:
            super().keyPressEvent(event)

    def add_items(self, *__labels: str) -> None:
        self.listWidget.clear()
        self.listWidget.addItems([*__labels])


class Restarter(_Dialog):
    def __init__(self, __parent) -> None:
        super().__init__(__parent, "Do you want to restart the IDE to save the changes", "Restart")

        self.setMinimumWidth(500)

    def accept(self):
        restart_application()


class ThemeChanger(_ListChanger):
    def __init__(self, __parent, *__theme_names: str) -> None:
        super().__init__(__parent, *__theme_names)

    def change_theme(self, __name: str) -> None:
        print(self.get_path_by_name(__name))

    def get_path_by_name(self, __name: str) -> str:
        themes = {
            FileLoader.load_json(f"scr/data/themes/{i}")["name"] : f"scr/data/themes/{i}"
            for i in os.listdir("scr/data/themes")
        }
        print(themes)

        for i in range(self.listWidget.count()):
            if self.listWidget.item(i).text() == __name:
                return themes[__name]
