from scr.scripts import FileLoader, restart_application

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit,
    QListWidget
)
from PySide6.QtCore import Qt

import os
import json


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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.accept()

        else:
            super().keyPressEvent(event)


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
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.mainLayout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.listWidget.addItems([*__values])
        self.mainLayout.addWidget(self.listWidget)

        self.setLayout(self.mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Down and self.listWidget.currentRow() + 1 < self.listWidget.count():
            self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)

        elif event.key() == Qt.Key.Key_Up and self.listWidget.currentRow() > 0:
            self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)

        elif event.key() == Qt.Key.Key_Return:
            self.accept()

        else:
            super().keyPressEvent(event)

    def add_items(self, *__labels: str) -> None:
        self.listWidget.clear()
        self.listWidget.addItems([*__labels])

    def get_item_by_text(self, __label: str):
        for i in range(self.listWidget.count()):

            if self.listWidget.item(i).text() == __label:
                return self.listWidget.item(i)

    def show(self):
        super().show()

    def get_current_item(self):
        return self.listWidget.currentItem()


class Restarter(_Dialog):
    def __init__(self, __parent) -> None:
        super().__init__(__parent, "Do you want to restart the IDE to save the changes", "Restart")

        self.setMinimumWidth(500)
        self.__command = None

    def set_command_after_restart(self, __command):
        """This command will be reset after one use"""

        self.__command = __command

    def accept(self):
        self.__command()
        self.__command = None  # reset command

        restart_application()


class ThemeChanger(_ListChanger):
    def __init__(self, __parent, restarter: Restarter) -> None:
        super().__init__(__parent)

        self.restarter = restarter
        self.listWidget.itemClicked.connect(self.accept)

    @staticmethod
    def __save(__arg):
        with open("scr/data/settings.json", "w") as file:
            json.dump(__arg, file, indent=4)

    def change_theme(self, __name: str) -> None:
        self.close()

        settings = FileLoader.load_json("scr/data/settings.json")
        settings["theme"] = {
            "path": self.get_theme_path_by_name(__name),
            "name": __name
        }

        self.restarter.set_command_after_restart(lambda: self.__save(settings))
        self.restarter.show()

    def get_theme_path_by_name(self, __name: str) -> str:
        themes = {
            FileLoader.load_json(f"scr/data/themes/{i}")["name"]: f"scr/data/themes/{i}"
            for i in os.listdir("scr/data/themes")
        }

        for i in range(self.listWidget.count()):
            if self.listWidget.item(i).text() == __name:
                return themes[__name]

    def show(self):
        current_theme = FileLoader.load_json("scr/data/settings.json")["theme"]["name"]

        super().show()
        self.listWidget.setCurrentItem(self.get_item_by_text(current_theme))

    def accept(self):
        self.change_theme(self.get_current_item().text())
