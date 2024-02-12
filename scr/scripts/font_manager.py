from scr.scripts import FileLoader

import json


class _FontManager:
    font_updater = None
    directory = None

    @classmethod
    def get_current_font(cls) -> dict:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]

    @classmethod
    def get_current_family(cls) -> str:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]["family"]

    @classmethod
    def get_current_font_size(cls) -> int:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]["size"]

    @classmethod
    def is_current_bold(cls) -> bool:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]["bold"]

    @classmethod
    def is_current_italic(cls) -> bool:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]["italic"]

    @classmethod
    def set_font_updater(cls, __changer):
        cls.font_updater = __changer

    @classmethod
    def set_current_font(cls, family: str | None = None, size: int | None = None, bold: bool | None = None, italic: bool | None = None):
        data = FileLoader.load_json("scr/data/settings.json")

        if family is None: family = cls.get_current_family()
        if size is None: size = cls.get_current_font_size()
        if bold is None: bold = data[cls.directory]["font"]["bold"]
        if italic is None: italic = data[cls.directory]["font"]["italic"]

        data[cls.directory]["font"] = {
            "family": family,
            "size": size,
            "bold": bold,
            "italic": italic,
        }

        with open("scr/data/settings.json", "w") as file:
            json.dump(data, file, indent=4)

        if cls.font_updater is not None: cls.font_updater()


class EditorFontManager(_FontManager):
    directory = "editor"


class WorkbenchFontManager(_FontManager):
    directory = "workbench"
