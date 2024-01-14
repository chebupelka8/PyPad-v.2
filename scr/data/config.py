from PySide6.QtGui import QTextCharFormat, QFont, QColor

from scr.scripts import FileLoader


WINDOW_SIZE = (1200, 800)
VERSION = "2.0 alpha"


class IconPaths:

    class FileIcons:
        PYTHON = "assets/icons/file_icons/python.png"
        CSS = "assets/icons/file_icons/css.png"
        JSON = "assets/icons/file_icons/son.png"
        TXT = "assets/icons/file_icons/txt.png"
        PICTURE = "assets/icons/file_icons/image.png"

    class SystemIcons:
        MAIN = "assets/icons/system_icons/window_icon.png"

    class FolderIcons:
        DEFAULT = "assets/icons/folder_icons/default_folder.ico"


class PythonPatterns:
    KEYWORDS = r"""\b(and|as|assert|async|await|break|class|continue
    |def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal
    |not|or|pass|raise|return|try|while|with|yield|case)\b"""

    CLASS_NAME = r"^\s*class .*"

    FUNCTION_NAME = r"^\s*def \w*\(.*\).*:"

    PYTHON_FUNCTIONS = r"""\b(divmod|map|filter|zip|super|open|help|hex|abs|eval|exec|ord|chr|sorted
    |reversed|enumerate|range|sum|repr|round|type|all|any)\b"""

    BOOLEAN = r"\b(True|False)\b"
    NONE_TYPE = r"\b(None)\b"
    DATA_TYPES = r"\b(int|float|str|dict|set|tuple|list|bool)\b"

    SPECIAL_SELF = r"\b(self|cls)\b"

    BRACKETS = r"\(|\)|\[|\]|\{|\}"
    DIGITS = r"1|2|3|4|5|6|7|8|9|0"
    PYTHON_SYMBOLS = r"\=|\+|\-|\>|\&|\<|\%|\/|\*|\|"

    DECORATOR = r"@.*$"
    COMMENT = r"#.*$"

    STRING_DOUBLE_QUOTATION = r'".*?\n*?"|".*?'
    STRING_APOSTROPHE = r"'.*?'|'.*?"
    LONG_STRING = r'""".*?"""|""".*?'


class JsonPatterns:
    STRING = r'".*?\n*?"|".*?'
    BRACKETS = r"\[|\]|\{|\}"
    BOOLEAN = r"\b(true|false)\b"
    SYMBOLS = r"\,\:"
    DIGITS = r"1|2|3|4|5|6|7|8|9|0"
    NULL_TYPE = r"\b(null)\b"


class StylePatterns:
    BRACKETS = r"\[|\]|\{|\}|\(|\)"
    SYMBOLS = r"\,\:"
    DIGITS = r"1|2|3|4|5|6|7|8|9|0"


class TextCharCreator:

    @staticmethod
    def create_char_format(__color: str, italic: bool = False, bold: bool = False) -> QTextCharFormat:
        res = QTextCharFormat()
        res.setForeground(QColor(__color))
        res.setFontItalic(italic)
        if bold:
            res.setFontWeight(QFont.Bold)

        return res


class TextEditorTheme:
    theme = FileLoader.load_json("scr/data/theme.json")["text-editor-theme"]

    DEFAULT = theme["default"]


class PythonTheme:
    theme = FileLoader.load_json("scr/data/theme.json")["python-theme"]

    DEFAULT = theme["default"]
    KEYWORDS = TextCharCreator.create_char_format(*theme["keywords"].values())
    STRING = TextCharCreator.create_char_format(*theme["string"].values())
    COMMENT = TextCharCreator.create_char_format(*theme["comment"].values())
    DECORATOR = TextCharCreator.create_char_format(*theme["decorator"].values())
    CLASS_NAMES = TextCharCreator.create_char_format(*theme["class-names"].values())
    FUNC_NAMES = TextCharCreator.create_char_format(*theme["func-names"].values())
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    BOOLEAN = TextCharCreator.create_char_format(*theme["boolean"].values())
    NONE_TYPE = TextCharCreator.create_char_format(*theme["none-type"].values())
    DATA_TYPES = TextCharCreator.create_char_format(*theme["data-types"].values())
    FUNCTIONS = TextCharCreator.create_char_format(*theme["functions"].values())
    DIGITS = TextCharCreator.create_char_format(*theme["digits"].values())
    BRACKETS = TextCharCreator.create_char_format(*theme["brackets"].values())
    SPECIAL = TextCharCreator.create_char_format(*theme["special"].values())


class JsonTheme:
    theme = FileLoader.load_json("scr/data/theme.json")["json-theme"]

    DEFAULT = theme["default"]
    STRING = TextCharCreator.create_char_format(*theme["string"].values())
    BOOLEAN = TextCharCreator.create_char_format(*theme["boolean"].values())
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    DIGITS = TextCharCreator.create_char_format(*theme["digits"].values())
    BRACKETS = TextCharCreator.create_char_format(*theme["brackets"].values())
    NULL_TYPE = TextCharCreator.create_char_format(*theme["null-type"].values())


class StyleTheme:
    theme = FileLoader.load_json("scr/data/theme.json")["style-theme"]

    DEFAULT = theme["default"]
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    DIGITS = TextCharCreator.create_char_format(*theme["digits"].values())
    BRACKETS = TextCharCreator.create_char_format(*theme["brackets"].values())
