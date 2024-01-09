from scr.scripts import PythonPatterns, ThemeColors

from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QColor
import re


class TextCharCreator:

    @staticmethod
    def create_char_format(__color: str, italic: bool = False, bold: bool = False) -> QTextCharFormat:
        res = QTextCharFormat()
        res.setForeground(QColor(__color))
        res.setFontItalic(italic)
        if bold:
            res.setFontWeight(QFont.Bold)

        return res


class CodeHighlighter(QSyntaxHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

        self.keyword_format = TextCharCreator.create_char_format(ThemeColors.KEYWORDS)
        self.function_format = TextCharCreator.create_char_format(ThemeColors.PYTHON_FUNCTIONS)
        self.logical_format = TextCharCreator.create_char_format(ThemeColors.BOOLEAN)
        self.string_format = TextCharCreator.create_char_format(ThemeColors.STRING_APOSTROPHE)
        self.special_format = TextCharCreator.create_char_format(ThemeColors.SPECIAL_SELF)
        self.decorator_format = TextCharCreator.create_char_format(ThemeColors.DECORATOR)
        self.data_types_format = TextCharCreator.create_char_format(ThemeColors.DATA_TYPES)
        self.brackets_format = TextCharCreator.create_char_format(ThemeColors.BRACKETS)
        self.comments_format = TextCharCreator.create_char_format(ThemeColors.COMMENT)
        self.symbols_format = TextCharCreator.create_char_format(ThemeColors.PYTHON_SYMBOLS)
        self.numbers_format = TextCharCreator.create_char_format(ThemeColors.DIGITS)
        self.classes_format = TextCharCreator.create_char_format(ThemeColors.CLASS_NAME)
        self.def_func_format = TextCharCreator.create_char_format(ThemeColors.FUNCTION_NAME)

    def highlightBlock(self, text):
        self.__highlight_match(PythonPatterns.CLASS_NAME, self.classes_format, text)
        self.__highlight_match(PythonPatterns.FUNCTION_NAME, self.def_func_format, text)
        self.__highlight_match(PythonPatterns.KEYWORDS, self.keyword_format, text)
        self.__highlight_match(PythonPatterns.PYTHON_FUNCTIONS, self.function_format, text)
        self.__highlight_match(PythonPatterns.BOOLEAN, self.logical_format, text)
        self.__highlight_match(PythonPatterns.NONE_TYPE, self.logical_format, text)
        self.__highlight_match(PythonPatterns.DATA_TYPES, self.data_types_format, text)
        self.__highlight_match(PythonPatterns.BRACKETS, self.brackets_format, text)
        self.__highlight_match(PythonPatterns.SPECIAL_SELF, self.special_format, text)
        self.__highlight_match(PythonPatterns.DIGITS, self.numbers_format, text)
        self.__highlight_match(PythonPatterns.PYTHON_SYMBOLS, self.symbols_format, text)
        self.__highlight_match(PythonPatterns.DECORATOR, self.decorator_format, text)
        self.__highlight_match(PythonPatterns.COMMENT, self.comments_format, text)
        self.__highlight_match(PythonPatterns.STRING_DOUBLE_QUOTATION, self.string_format, text)
        self.__highlight_match(PythonPatterns.STRING_APOSTROPHE, self.string_format, text)
        self.__highlight_match(PythonPatterns.LONG_STRING, self.string_format, text)

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
