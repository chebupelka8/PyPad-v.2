from scr.scripts import FileLoader, CodeHighlighter, CodeAnalyzer
from .text_area import TextEditorArea

from PySide6.QtCore import Qt


class PythonCodeEditorArea(TextEditorArea):
    def __init__(self, __path: str | None = None):
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/editor_area.css"))
        self.setObjectName("code-area")

        if __path != None:
            self.insertPlainText(FileLoader.load_python_file(__path))

        CodeHighlighter(self)  # set highlighter

    def __insert_around_cursor(self, __symbol_1: str, __symbol_2: str) -> None:
        cursor = self.textCursor()
        selected_text = cursor.selectedText()

        cursor.insertText(f"{selected_text}".join([__symbol_1, __symbol_2]))
        cursor.setPosition(cursor.position() - 1)
        self.setTextCursor(cursor)

    def __pass_duplicate_symbol(self, __target: str) -> None | str:
        cursor = self.textCursor()

        if len(self.toPlainText().split("\n")[self.get_current_line()][cursor.positionInBlock():]) != 0:

            if self.toPlainText().split("\n")[self.get_current_line()][cursor.positionInBlock()] == __target:
                cursor.setPosition(cursor.position() + 1)
                self.setTextCursor(cursor)

            else:
                return "exception"

        else:
            return "exception"

    def keyPressEvent(self, event):
        self.lineNumberArea.update()  # update number area

        if event.key() == Qt.Key.Key_ParenLeft:
            self.__insert_around_cursor("(", ")")

        elif event.key() == Qt.Key.Key_BraceLeft:
            self.__insert_around_cursor("{", "}")

        elif event.key() == Qt.Key.Key_BracketLeft:
            self.__insert_around_cursor("[", "]")

        elif event.key() == Qt.Key.Key_QuoteDbl:
            self.__insert_around_cursor('"', '"')

        elif event.key() == Qt.Key.Key_Apostrophe:
            self.__insert_around_cursor("'", "'")

        elif event.key() == Qt.Key.Key_ParenRight:
            if self.__pass_duplicate_symbol(")") == "exception":
                super().keyPressEvent(event)

        elif event.key() == Qt.Key.Key_BraceRight:
            if self.__pass_duplicate_symbol("}") == "exception":
                super().keyPressEvent(event)

        elif event.key() == Qt.Key.Key_BracketRight:
            if self.__pass_duplicate_symbol("]") == "exception":
                super().keyPressEvent(event)

        elif event.key() == Qt.Key.Key_Tab:
            self.textCursor().insertText("    ")

        elif event.key() == Qt.Key.Key_Return:
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
                super().keyPressEvent(event)

        else:
            super().keyPressEvent(event)


class JsonCodeEditorArea(TextEditorArea):
    def __init__(self, __path: str | None = None):
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/editor_area.css"))
        self.setObjectName("code-area")

        if __path != None:
            self.insertPlainText(FileLoader.load_json_file(__path))
