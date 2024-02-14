from scr.scripts import EditorFontManager, FileLoader, Font, WorkbenchFontManager

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout,
    QComboBox, QLabel, QSizePolicy, QSpinBox,
    QSpacerItem, QDialog, QCheckBox, QFrame,
    QScrollArea, QWidget, QListWidget
)
from PySide6.QtCore import Qt


class SettingFrame(QFrame):
    def __init__(self, __title: str, __description: str) -> None:
        super().__init__()

        self.setObjectName("setting-frame")
        self.mainLayout = QVBoxLayout()
        self.setMinimumHeight(100)

        self.mainLayout.addWidget(self.__title(__title))
        self.mainLayout.addWidget(self.__description(__description))
        q = QComboBox()
        q.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        q.setFixedWidth(200)
        q.addItems(Font.get_all_font_families())
        self.mainLayout.addWidget(q)

        self.setLayout(self.mainLayout)

    @staticmethod
    def __title(__text: str) -> QLabel:
        label = QLabel(__text)
        label.setFont(Font.get_font_by_path("assets/fonts/CascadiaMono.ttf", 14))

        return label

    @staticmethod
    def __description(__text: str) -> QLabel:
        label = QLabel(__text)
        label.setFont(Font.get_font_by_path("assets/fonts/CascadiaMono.ttf", 10))

        return label


class MainSettingsWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.setObjectName("main-settings-widget")
        self.setMinimumWidth(800)

        self.mainLayout.addWidget(SettingFrame("Editor: <b>Font Size</b>", "Defines the font size in pixels"))
        self.mainLayout.addWidget(SettingFrame("Editor: <b>Family</b>", "Defines the font family"))
        self.mainLayout.addWidget(SettingFrame("Editor: <b>Cursor</b>", "Controls the cursor"))
        self.mainLayout.addWidget(SettingFrame("Editor: <b>Cursor</b>", "Controls the cursor"))
        self.mainLayout.addWidget(SettingFrame("Editor: <b>Cursor</b>", "Controls the cursor"))
        self.mainLayout.addWidget(SettingFrame("Editor: <b>Cursor</b>", "Controls the cursor"))
        self.mainLayout.addWidget(SettingFrame("Editor: <b>Cursor</b>", "Controls the cursor"))
        # self.mainLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        self.setLayout(self.mainLayout)

        # self.setLayout(self.mainLayout)


class SettingTree(QListWidget):
    def __init__(self):
        super().__init__()

        self.update_font()
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def update_font(self) -> None:
        self.__main_font = Font.get_system_font(
            WorkbenchFontManager.get_current_family(), WorkbenchFontManager.get_current_font_size()
        )
        self.setFont(self.__main_font)


class SettingsMenu(QDialog):
    def __init__(self, __parent) -> None:
        super().__init__(__parent)

        self.setWindowTitle("Settings")
        self.setMinimumSize(840, 400)
        self.setStyleSheet(FileLoader.load_style("scr/styles/settings_menu.css"))

        self.settingsArea = QScrollArea()
        self.settingsArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.mainSettingsWidget = MainSettingsWidget()
        self.settingsArea.setWidget(self.mainSettingsWidget)

        self.settingTree = SettingTree()
        self.settingTree.addItems(["Main", "Editor", "Theme", "Interpreter"])

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.settingTree, stretch=1)
        self.mainLayout.addWidget(self.settingsArea, stretch=3)

        self.setLayout(self.mainLayout)
        # self.fontLayout = QHBoxLayout()
        # self.sizeFontLayout = QHBoxLayout()
        # self.boldLayout = QHBoxLayout()
        # self.italicLayout = QHBoxLayout()
        #
        # self.mainLayout.addWidget(SettingFrame("Editor: <b>Font Size</b>", "Defines the font size in pixels"))
        # self.mainLayout.addWidget(SettingFrame("Editor: <b>Family</b>", "Defines the font family"))
        # self.mainLayout.addWidget(SettingFrame("Editor: <b>Cursor</b>", "Controls the cursor"))
        #
        # self.font_changer = QComboBox()
        # self.font_changer.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.font_changer.addItems(Font.get_all_font_families())
        #
        # self.font_size_changer = QSpinBox()
        # self.font_size_changer.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        #
        # self.is_bold = QCheckBox()
        # self.is_italic = QCheckBox()
        #
        # # to layouts
        # # font
        # self.mainLayout.addWidget(self.__h1_label("Main"))
        # self.mainLayout.addWidget(self.__h2_label("Font"))
        #
        # # editor font
        # self.mainLayout.addWidget(self.__h1_label("Editor"))
        # self.mainLayout.addWidget(self.__h2_label("Font"))
        # self.fontLayout.addWidget(self.__name_label("Family:"))
        # self.fontLayout.addWidget(self.font_changer)
        # self.fontLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))
        #
        # self.sizeFontLayout.addWidget(self.__name_label("Size:"))
        # self.sizeFontLayout.addWidget(self.font_size_changer)
        # self.sizeFontLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))
        #
        # self.boldLayout.addWidget(self.__name_label("Bold:"))
        # self.boldLayout.addItem(QSpacerItem(10, 0))
        # self.boldLayout.addWidget(self.is_bold)
        # self.boldLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))
        #
        # self.italicLayout.addWidget(self.__name_label("Italic:"))
        # self.italicLayout.addItem(QSpacerItem(10, 0))
        # self.italicLayout.addWidget(self.is_italic)
        # self.italicLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))
        #
        # self.mainLayout.addLayout(self.fontLayout)
        # self.mainLayout.addLayout(self.sizeFontLayout)
        # self.mainLayout.addLayout(self.boldLayout)
        # self.mainLayout.addLayout(self.italicLayout)
        # self.mainLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding))


    #     # connections
    #     self.font_changer.currentTextChanged.connect(lambda text: EditorFontManager.set_current_font(family=text))
    #     self.font_size_changer.valueChanged.connect(lambda value: EditorFontManager.set_current_font(size=value))
    #     self.is_bold.stateChanged.connect(lambda __is: EditorFontManager.set_current_font(bold=bool(__is)))
    #     self.is_italic.stateChanged.connect(lambda __is: EditorFontManager.set_current_font(italic=bool(__is)))
    #
    # def __update_values(self) -> None:
    #     self.font_changer.setCurrentText(EditorFontManager.get_current_family())
    #     self.font_size_changer.setValue(EditorFontManager.get_current_font_size())
    #
    #     if EditorFontManager.is_current_bold():
    #         self.is_bold.setCheckState(Qt.CheckState.Checked)
    #     else: self.is_bold.setCheckState(Qt.CheckState.Unchecked)
    #
    #     if EditorFontManager.is_current_italic():
    #         self.is_italic.setCheckState(Qt.CheckState.Checked)
    #     else: self.is_italic.setCheckState(Qt.CheckState.Unchecked)
    #
    # @staticmethod
    # def __h1_label(__text: str) -> QLabel:
    #     label = QLabel(__text)
    #     label.setFont(Font.get_font_by_path("assets/fonts/CascadiaMono.ttf", 18, True))
    #
    #     return label
    #
    # @staticmethod
    # def __h2_label(__text: str) -> QLabel:
    #     label = QLabel(__text)
    #     label.setContentsMargins(20, 0, 0, 0)
    #     label.setFont(Font.get_font_by_path("assets/fonts/CascadiaMono.ttf", 14, False))
    #
    #     return label
    #
    # @staticmethod
    # def __name_label(__text: str):
    #     label = QLabel(__text)
    #     label.setContentsMargins(40, 0, 0, 0)
    #
    #     return label
    #
    # def show(self):
    #     self.__update_values()
    #     super().show()