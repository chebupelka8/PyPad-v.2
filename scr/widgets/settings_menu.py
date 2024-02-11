from scr.scripts import FontManager, FileLoader

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout,
    QComboBox, QLabel, QSizePolicy, QSpinBox,
    QSpacerItem, QDialog, QCheckBox
)
from PySide6.QtCore import Qt


class SettingsMenu(QDialog):
    def __init__(self, __parent) -> None:
        super().__init__(__parent)

        self.setWindowTitle("Settings")
        self.setMinimumSize(800, 400)
        self.setStyleSheet(
            FileLoader.load_style("scr/styles/settings_menu.css") + FileLoader.load_style("scr/styles/ui.css")
        )

        self.mainLayout = QVBoxLayout()
        self.fontLayout = QHBoxLayout()
        self.sizeFontLayout = QHBoxLayout()
        self.boldLayout = QHBoxLayout()
        self.italicLayout = QHBoxLayout()

        self.mainLayout.addWidget(self.__h1_label("Font"))

        self.font_changer = QComboBox()
        self.font_changer.addItems(FontManager.get_all_font_families())

        self.font_size_changer = QSpinBox()
        self.font_size_changer.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        self.is_bold = QCheckBox()
        self.is_italic = QCheckBox()

        # to layouts
        self.fontLayout.addWidget(self.__name_label("Family:"))
        self.fontLayout.addWidget(self.font_changer)
        self.fontLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))

        self.sizeFontLayout.addWidget(self.__name_label("Size:"))
        self.sizeFontLayout.addWidget(self.font_size_changer)
        self.sizeFontLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))

        self.boldLayout.addWidget(self.__name_label("Bold:"))
        self.boldLayout.addItem(QSpacerItem(10, 0))
        self.boldLayout.addWidget(self.is_bold)
        self.boldLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))

        self.italicLayout.addWidget(self.__name_label("Italic:"))
        self.italicLayout.addItem(QSpacerItem(10, 0))
        self.italicLayout.addWidget(self.is_italic)
        self.italicLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))

        self.mainLayout.addLayout(self.fontLayout)
        self.mainLayout.addLayout(self.sizeFontLayout)
        self.mainLayout.addLayout(self.boldLayout)
        self.mainLayout.addLayout(self.italicLayout)
        self.mainLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding))

        self.setLayout(self.mainLayout)

        # connections
        self.font_changer.currentTextChanged.connect(lambda text: FontManager.set_current_font(family=text))
        self.font_size_changer.valueChanged.connect(lambda value: FontManager.set_current_font(size=value))
        self.is_bold.stateChanged.connect(lambda __is: FontManager.set_current_font(bold=bool(__is)))
        self.is_italic.stateChanged.connect(lambda __is: FontManager.set_current_font(italic=bool(__is)))

    def __update_values(self) -> None:
        self.font_changer.setCurrentText(FontManager.get_current_family())
        self.font_size_changer.setValue(FontManager.get_current_font_size())

        if FontManager.is_current_bold():
            self.is_bold.setCheckState(Qt.CheckState.Checked)
        else: self.is_bold.setCheckState(Qt.CheckState.Unchecked)

        if FontManager.is_current_italic():
            self.is_italic.setCheckState(Qt.CheckState.Checked)
        else: self.is_italic.setCheckState(Qt.CheckState.Unchecked)

    @staticmethod
    def __h1_label(__text: str) -> QLabel:
        label = QLabel(__text)
        label.setFont(FontManager.get_font_by_path("assets/fonts/CascadiaMono.ttf", 18, True, False))

        return label

    @staticmethod
    def __name_label(__text: str):
        label = QLabel(__text)
        label.setContentsMargins(20, 0, 0, 0)

        return label

    def show(self):
        self.__update_values()
        super().show()