WINDOW_SIZE = (1200, 800)
VERSION = "2.0 alpha"


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


class ThemeColors:

    DEFAULT = "#ffffff"

    KEYWORDS = "#dd6f66"

    CLASS_NAME = "#87bba2"

    FUNCTION_NAME = "#c7bcfa"

    PYTHON_FUNCTIONS = "#fabd2f"

    BOOLEAN = "#dd6f66"
    NONE_TYPE = "#dd6f66"
    DATA_TYPES = "#fabd2f"

    SPECIAL_SELF = "#f59c47"

    BRACKETS = DEFAULT
    DIGITS = DEFAULT
    PYTHON_SYMBOLS = KEYWORDS

    DECORATOR = "#dcbdfb"
    COMMENT = "#768390"

    STRING_DOUBLE_QUOTATION = "#84a98c"
    STRING_APOSTROPHE = STRING_DOUBLE_QUOTATION
    LONG_STRING = STRING_DOUBLE_QUOTATION
