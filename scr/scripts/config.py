from faker import Faker


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

    SPECIAL_SELF = r"\b(self)\b"

    BRACKETS = r"\(|\)|\[|\]|\{|\}"
    DIGITS = r"1|2|3|4|5|6|7|8|9|0"
    PYTHON_SYMBOLS = r"\=|\+|\-|\>|\&|\<|\%|\/|\*|\|"

    DECORATOR = r"@.*$"
    COMMENT = r"#.*$"

    STRING_DOUBLE_QUOTATION = r'".*?\n*?"|".*?'
    STRING_APOSTROPHE = r"'.*?'|'.*?"
    LONG_STRING = r'""".*?"""|""".*?'


class ThemeColors:
    fake = Faker()

    KEYWORDS = fake.hex_color()

    CLASS_NAME = fake.hex_color()

    FUNCTION_NAME = fake.hex_color()

    PYTHON_FUNCTIONS = fake.hex_color()

    BOOLEAN = fake.hex_color()
    NONE_TYPE = fake.hex_color()
    DATA_TYPES = fake.hex_color()

    SPECIAL_SELF = fake.hex_color()

    BRACKETS = fake.hex_color()
    DIGITS = fake.hex_color()
    PYTHON_SYMBOLS = fake.hex_color()

    DECORATOR = fake.hex_color()
    COMMENT = fake.hex_color()

    STRING_DOUBLE_QUOTATION = fake.hex_color()
    STRING_APOSTROPHE = fake.hex_color()
    LONG_STRING = fake.hex_color()
