from scr.scripts import (
    FileLoader, PythonCodeHighlighter, CodeAnalyzer,
    JsonCodeHighLighter, StyleCodeHighLighter, HtmlCodeHighlighter
)
from scr.data import PythonTheme, JsonTheme, StyleTheme
from .text_area import TextEditorArea

from PySide6.QtCore import Qt


class CodeEditorArea(TextEditorArea):
    def __init__(self):
        super().__init__()

    def insert_around_cursor(self, __symbol_1: str, __symbol_2: str) -> None:
        cursor = self.textCursor()
        selected_text = cursor.selectedText()

        cursor.insertText(f"{selected_text}".join([__symbol_1, __symbol_2]))
        cursor.setPosition(cursor.position() - 1)
        self.setTextCursor(cursor)

    def pass_duplicate_symbol(self, __target: str) -> None | str:
        cursor = self.textCursor()

        if len(self.toPlainText().split("\n")[self.get_current_line()][cursor.positionInBlock():]) != 0:

            if self.toPlainText().split("\n")[self.get_current_line()][cursor.positionInBlock()] == __target:
                cursor.setPosition(cursor.position() + 1)
                self.setTextCursor(cursor)

            else:
                return "exception"

        else:
            return "exception"

    def key_press_filter(
            self, __event,
            paren: bool = False,
            brace: bool = False,
            bracket: bool = False,
            quote_dbl: bool = False,
            apostrophe: bool = False,
            tag: bool = False
    ):

        self.lineNumberArea.update()

        if __event.key() == Qt.Key.Key_ParenLeft and paren:
            self.insert_around_cursor("(", ")")

        elif __event.key() == Qt.Key.Key_ParenRight and paren:
            if self.pass_duplicate_symbol(")") == "exception":
                super().keyPressEvent(__event)

        elif __event.key() == Qt.Key.Key_BraceLeft and brace:
            self.insert_around_cursor("{", "}")

        elif __event.key() == Qt.Key.Key_BraceRight and brace:
            if self.pass_duplicate_symbol("}") == "exception":
                super().keyPressEvent(__event)

        elif __event.key() == Qt.Key.Key_BracketLeft and bracket:
            self.insert_around_cursor("[", "]")

        elif __event.key() == Qt.Key.Key_BracketRight and bracket:
            if self.pass_duplicate_symbol("]") == "exception":
                super().keyPressEvent(__event)

        elif __event.key() == Qt.Key.Key_Less and tag:
            self.insert_around_cursor("<", ">")

        elif __event.key() == Qt.Key.Key_Greater and tag:
            if self.pass_duplicate_symbol(">") == "exception":
                super().keyPressEvent(__event)

        elif __event.key() == Qt.Key.Key_QuoteDbl and quote_dbl:
            self.insert_around_cursor('"', '"')

        elif __event.key() == Qt.Key.Key_Apostrophe and apostrophe:
            self.insert_around_cursor("'", "'")

        elif __event.key() == Qt.Key.Key_Tab:
            self.textCursor().insertText("    ")

        else:
            super().keyPressEvent(__event)


class PythonCodeEditorArea(CodeEditorArea):
    def __init__(self, __path: str | None = None):
        super().__init__()

        self.__path = __path

        self.setStyleSheet(FileLoader.load_style("scr/styles/editor_area.css"))
        self.setObjectName("code-area")

        if __path != None:
            # self.highlight_insert(FileLoader.load_python_file(__path))
            self.insertPlainText(FileLoader.load_python_file(__path))

        PythonCodeHighlighter(self)  # set highlighter
        self.set_default_text_color(PythonTheme.DEFAULT)

    def get_full_path(self):
        return self.__path

    def keyPressEvent(self, event):
        key_func = lambda: (
            self.key_press_filter(event, True, True, True, True, True))

        if event.key() == Qt.Key.Key_Return:
            cursor = self.textCursor()
            previous = self.toPlainText().split("\n")[cursor.blockNumber()]

            if previous == "":
                prev = "//"  # it's need for remove exception - list has no index -1

            elif not previous.isspace() and previous.replace(" ", "") != "":
                try:
                    prev = previous[:cursor.positionInBlock()].rstrip()
                    prev[-1]  # checks if there is a character at the end of the line

                except IndexError:
                    prev = "//none"
            else:
                prev = previous

            if prev[-1] == ":" or self.toPlainText().split("\n")[cursor.blockNumber()][:4] == "    ":
                tab_count = (CodeAnalyzer.find_tabs_in_string(previous) +
                             CodeAnalyzer.check_last_character_is_colon(prev))
                cursor.insertText("\n" + ("    " * tab_count))

            else:
                key_func()

        else:
            key_func()


class JsonCodeEditorArea(CodeEditorArea):
    def __init__(self, __path: str | None = None):
        super().__init__()

        self.__path = __path

        self.setStyleSheet(FileLoader.load_style("scr/styles/editor_area.css"))
        self.setObjectName("code-area")

        if __path != None:
            self.insertPlainText(FileLoader.load_json_text(__path))

        JsonCodeHighLighter(self)
        self.set_default_text_color(JsonTheme.DEFAULT)

    def get_full_path(self):
        return self.__path

    def keyPressEvent(self, event):
        self.key_press_filter(event, False, True, True, True, False)


class StyleCodeEditorArea(CodeEditorArea):
    def __init__(self, __path: str):
        super().__init__()

        self.__path = __path

        self.setStyleSheet(FileLoader.load_style("scr/styles/editor_area.css"))
        self.setObjectName("code-area")

        if __path != None:
            self.insertPlainText(FileLoader.load_style(__path))

        StyleCodeHighLighter(self)
        self.set_default_text_color(StyleTheme.DEFAULT)

    def get_full_path(self):
        return self.__path

    def keyPressEvent(self, event):
        self.key_press_filter(event, True, False, True, True, True)


class HtmlCodeEditorArea(CodeEditorArea):
    def __init__(self, __path: str | None = None):
        super().__init__()

        self.__path = __path

        self.setStyleSheet(FileLoader.load_style("scr/styles/editor_area.css"))
        self.setObjectName("code-area")

        if __path != None:
            self.insertPlainText(FileLoader.load_html(__path))

        HtmlCodeHighlighter(self)

    def get_full_path(self):
        return self.__path

    def keyPressEvent(self, event):
        self.key_press_filter(event, False, False, False, True, True, True)
