from scr.scripts import FontManager, FileLoader

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout,
    QComboBox, QLabel, QSizePolicy, QSpinBox,
    QSpacerItem, QDialog
)


class SettingsMenu(QDialog):
    def __init__(self, __parent) -> None:
        super().__init__(__parent)

        self.setMinimumSize(400, 200)
        self.setStyleSheet(
            FileLoader.load_style("scr/styles/settings_menu.css") + FileLoader.load_style("scr/styles/ui.css")
        )

        self.mainLayout = QVBoxLayout()
        self.fontLayout = QHBoxLayout()
        self.sizeFontLayout = QHBoxLayout()

        self.font_changer = QComboBox()
        self.font_changer.addItems(FontManager.get_all_font_families())
        self.fontLayout.addWidget(QLabel("  Family:"))
        self.fontLayout.addWidget(self.font_changer)
        self.fontLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))

        self.font_size_changer = QSpinBox()
        self.sizeFontLayout.addWidget(QLabel("  Size:"))
        self.sizeFontLayout.addWidget(self.font_size_changer)
        self.sizeFontLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))

        self.mainLayout.addLayout(self.fontLayout)
        self.mainLayout.addLayout(self.sizeFontLayout)
        self.mainLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding))

        self.setLayout(self.mainLayout)

        self.font_changer.currentTextChanged.connect(lambda text: FontManager.set_current_font(family=text))
        self.font_size_changer.valueChanged.connect(lambda value: FontManager.set_current_font(size=value))

    def __update_values(self) -> None:
        self.font_changer.setCurrentText(FontManager.get_current_family())
        self.font_size_changer.setValue(FontManager.get_current_font_size())

    def show(self):
        self.__update_values()
        super().show()