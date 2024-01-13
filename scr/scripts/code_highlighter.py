from scr.data import PythonPatterns, PythonTheme, JsonPatterns, JsonTheme, StylePatterns, StyleTheme

from PySide6.QtGui import QSyntaxHighlighter

import re


class PythonCodeHighlighter(QSyntaxHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.__highlight_match(PythonPatterns.CLASS_NAME, PythonTheme.CLASS_NAMES, text)
        self.__highlight_match(PythonPatterns.FUNCTION_NAME, PythonTheme.FUNC_NAMES, text)
        self.__highlight_match(PythonPatterns.KEYWORDS, PythonTheme.KEYWORDS, text)
        self.__highlight_match(PythonPatterns.PYTHON_FUNCTIONS, PythonTheme.FUNCTIONS, text)
        self.__highlight_match(PythonPatterns.BOOLEAN, PythonTheme.BOOLEAN, text)
        self.__highlight_match(PythonPatterns.NONE_TYPE, PythonTheme.NONE_TYPE, text)
        self.__highlight_match(PythonPatterns.DATA_TYPES, PythonTheme.DATA_TYPES, text)
        self.__highlight_match(PythonPatterns.BRACKETS, PythonTheme.BRACKETS, text)
        self.__highlight_match(PythonPatterns.SPECIAL_SELF, PythonTheme.SPECIAL, text)
        self.__highlight_match(PythonPatterns.DIGITS, PythonTheme.DIGITS, text)
        self.__highlight_match(PythonPatterns.PYTHON_SYMBOLS, PythonTheme.SYMBOLS, text)
        self.__highlight_match(PythonPatterns.DECORATOR, PythonTheme.DECORATOR, text)
        self.__highlight_match(PythonPatterns.COMMENT, PythonTheme.COMMENT, text)
        self.__highlight_match(PythonPatterns.STRING_DOUBLE_QUOTATION, PythonTheme.STRING, text)
        self.__highlight_match(PythonPatterns.STRING_APOSTROPHE, PythonTheme.STRING, text)
        self.__highlight_match(PythonPatterns.LONG_STRING, PythonTheme.STRING, text)

    def __highlight_match(self, __pattern, __format, __text):
        for match in re.finditer(__pattern, __text):
            txt = match.group()

            if "def" in txt and "(" in txt:
                start = match.start() + 4
                count = len(txt[4:txt.find("(")])

            elif "class" in txt and ":" in txt:
                start = match.start() + 6

                if txt.find("(") != -1:
                    count = len(txt[6:txt.find("(")])
                else:
                    count = len(txt[6:txt.find(":")])

            else:
                start = match.start()
                count = match.end() - match.start()

            self.setFormat(start, count, __format)


class JsonCodeHighLighter(QSyntaxHighlighter):
    def __init__(self, target) -> None:
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.__highlight_match(JsonPatterns.DIGITS, JsonTheme.DIGITS, text)
        self.__highlight_match(JsonPatterns.BOOLEAN, JsonTheme.BOOLEAN, text)
        self.__highlight_match(JsonPatterns.NULL_TYPE, JsonTheme.NULL_TYPE, text)
        self.__highlight_match(JsonPatterns.SYMBOLS, JsonTheme.SYMBOLS, text)
        self.__highlight_match(JsonPatterns.BRACKETS, JsonTheme.BRACKETS, text)
        self.__highlight_match(JsonPatterns.STRING, JsonTheme.STRING, text)

    def __highlight_match(self, __pattern, __format, __text):
        for match in re.finditer(__pattern, __text):
            start = match.start()
            count = match.end() - match.start()

            self.setFormat(start, count, __format)


class StyleCodeHighLighter(QSyntaxHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.__highlight_match(StylePatterns.DIGITS, StyleTheme.DIGITS, text)
        self.__highlight_match(StylePatterns.BRACKETS, StyleTheme.BRACKETS, text)
        self.__highlight_match(StylePatterns.SYMBOLS, StyleTheme.SYMBOLS, text)

    def __highlight_match(self, __pattern, __format, __text):
        for match in re.finditer(__pattern, __text):
            start = match.start()
            count = match.end() - match.start()

            self.setFormat(start, count, __format)
