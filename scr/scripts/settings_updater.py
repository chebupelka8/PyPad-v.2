from .file_loader import FileLoader

import json


class _SettingsUpdater:
    updaters = None
    directory = None

    @classmethod
    def get_settings(cls):
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]

    @classmethod
    def call_updaters(cls):
        for upd in cls.updaters:
            upd()

    @classmethod
    def add_updater(cls, __command):
        cls.updaters.append(__command)


class EditorSettingsUpdater(_SettingsUpdater):
    updaters = []
    directory = "editor"

    @classmethod
    def set_cursor_style(cls, __style: str) -> None:
        settings = FileLoader.load_json("scr/data/settings.json")

        settings["editor"]["cursor"]["style"] = __style

        with open("scr/data/settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)

        cls.call_updaters()

    @classmethod
    def get_cursor_style(cls) -> str:
        return cls.get_settings()["cursor"]["style"]


class WorkbenchSettingsUpdater(_SettingsUpdater):
    updaters = []
    directory = "workbench"
