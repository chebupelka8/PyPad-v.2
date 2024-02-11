from PySide6.QtGui import QFontDatabase, QFont


class FontManager:

    @staticmethod
    def get_all_font_families() -> list[str]:
        return QFontDatabase.families()

    @staticmethod
    def get_font_by_path(__path: str, __size: int) -> QFont:
        __id = QFontDatabase.addApplicationFont(__path)
        families = QFontDatabase.applicationFontFamilies(__id)

        return QFont(families[0], __size, 1, False)
