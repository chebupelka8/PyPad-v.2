from PySide6.QtGui import QFontDatabase, QFont

from scr.scripts import FileLoader

import json


class FontManager:
    __font_updater = None

    @staticmethod
    def get_all_font_families() -> list[str]:
        return QFontDatabase.families()

    @staticmethod
    def get_current_font() -> dict:
        return FileLoader.load_json("scr/data/settings.json")["font"]

    @staticmethod
    def get_current_family() -> str:
        return FileLoader.load_json("scr/data/settings.json")["font"]["family"]

    @staticmethod
    def get_current_font_size() -> int:
        return FileLoader.load_json("scr/data/settings.json")["font"]["size"]

    @staticmethod
    def is_current_bold() -> bool:
        return FileLoader.load_json("scr/data/settings.json")["font"]["bold"]

    @staticmethod
    def is_current_italic() -> bool:
        return FileLoader.load_json("scr/data/settings.json")["font"]["italic"]

    @classmethod
    def set_font_updater(cls, __changer):
        cls.__font_updater = __changer

    @classmethod
    def set_current_font(cls, family: str | None = None, size: int | None = None, bold: bool | None = None, italic: bool | None = None):
        data = FileLoader.load_json("scr/data/settings.json")

        if family is None: family = cls.get_current_family()
        if size is None: size = cls.get_current_font_size()
        if bold is None: bold = data["font"]["bold"]
        if italic is None: italic = data["font"]["italic"]

        data["font"] = {
            "family": family,
            "size": size,
            "bold": bold,
            "italic": italic,
        }

        with open("scr/data/settings.json", "w") as file:
            json.dump(data, file, indent=4)

        if cls.__font_updater is not None: cls.__font_updater()

    @staticmethod
    def get_font_by_path(__path: str, __size: int | float, __bold: bool = False, __italic: bool = False) -> QFont:
        __id = QFontDatabase.addApplicationFont(__path)
        families = QFontDatabase.applicationFontFamilies(__id)

        font = QFont(families[0], __size, 1, __italic)
        font.setBold(__bold)

        return font

    @staticmethod
    def get_system_font(__family: str, __size: int | float, __bold: bool = False, __italic: bool = False) -> QFont:
        font = QFont(__family, __size, 1, __italic)
        font.setBold(__bold)

        return font
