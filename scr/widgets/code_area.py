from scr.scripts import FileLoader, CodeHighlighter, CodeAnalyzer

from PySide6.QtWidgets import QPlainTextEdit, QTextEdit, QWidget
from PySide6.QtGui import QColor, QTextFormat, QPainter
from PySide6.QtCore import Qt, QRect, QSize, QPoint


class CodeEditorArea(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(FileLoader.load_style("scr/styles/code_area.css"))
        self.setObjectName("code-area")

        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        CodeHighlighter(self)  # set highlighter
        self.__highlight_current_line()

        # connections
        self.__update_line_number_area_width()
        self.blockCountChanged.connect(self.__update_line_number_area_width)
        self.cursorPositionChanged.connect(self.__update_current_line)
        self.cursorPositionChanged.connect(self.__highlight_current_line)
        self.textChanged.connect(self.__highlight_current_line())

        self.__lineNumberArea = LineNumPaint(self)

        # variables
        self.__current_line = 0

    def wheelEvent(self, delta) -> None:
        self.__lineNumberArea.update()
        super().wheelEvent(delta)

    def mousePressEvent(self, event) -> None:
        super().mousePressEvent(event)

        self.update()
        self.__lineNumberArea.update()
        self.__highlight_current_line()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        content_rect = self.contentsRect()
        self.__lineNumberArea.setGeometry(QRect(content_rect.left(),
                                                content_rect.top(),
                                                self.get_number_area_width(),
                                                content_rect.height()))

    def __update_line_number_area_width(self):
        self.setViewportMargins(self.get_number_area_width(), 0, 0, 0)

    def get_number_area_width(self) -> int:
        block_count = self.document().blockCount()
        max_value = max(1, block_count)
        d_count = len(str(max_value))
        width = self.fontMetrics().height() * d_count + 5

        return width

    def __highlight_current_line(self):
        extra_selections = []

        if not self.isReadOnly() and self.hasFocus():
            selection = QTextEdit.ExtraSelection()

            selection.format.setBackground(QColor("#303030"))
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()

            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)

    def __update_current_line(self):
        cursor = self.textCursor()
        self.__current_line = cursor.blockNumber()

    def line_number_area_paint_event(self, event):
        cursor = self.textCursor()
        painter = QPainter(self.__lineNumberArea)

        painter.fillRect(event.rect(), QColor("#272727"))
        line_height = self.fontMetrics().lineSpacing()

        block_number = self.cursorForPosition(QPoint(0, int(line_height / 2))).blockNumber()
        first_visible_block = self.document().findBlock(block_number)
        cursor.setPosition(self.cursorForPosition(QPoint(0, int(line_height / 2))).position())
        rect = self.cursorRect()
        scroll_compensation = rect.y() - int(rect.y() / line_height) * line_height
        top = scroll_compensation
        last_block_number = self.cursorForPosition(QPoint(0, self.height() - 1)).blockNumber()

        height = self.fontMetrics().height()
        block = first_visible_block

        while block.isValid() and (top <= event.rect().bottom()) and block_number <= last_block_number:
            if block.isVisible():
                number = str(block_number + 1)
                painter.setPen(QColor("#b3b3b3"))

                painter.drawText(0, top, self.__lineNumberArea.width(), height, Qt.AlignCenter, number)

            block = block.next()
            top = top + line_height
            block_number += 1

    def __insert_around_cursor(self, __symbol_1: str, __symbol_2: str) -> None:
        cursor = self.textCursor()
        selected_text = cursor.selectedText()

        cursor.insertText(f"{selected_text}".join([__symbol_1, __symbol_2]))
        cursor.setPosition(cursor.position() - 1)
        self.setTextCursor(cursor)

    def __pass_duplicate_symbol(self, __target: str) -> None | str:
        cursor = self.textCursor()

        if len(self.toPlainText().split("\n")[self.__current_line][cursor.positionInBlock():]) != 0:

            if self.toPlainText().split("\n")[self.__current_line][cursor.positionInBlock()] == __target:
                cursor.setPosition(cursor.position() + 1)
                self.setTextCursor(cursor)

            else:
                return "exception"

        else:
            return "exception"

    def keyPressEvent(self, event):
        self.__lineNumberArea.update()

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


class LineNumPaint(QWidget):
    def __init__(self, parent: CodeEditorArea):
        super().__init__(parent)

        self.setStyleSheet(FileLoader.load_style("scr/styles/line_number_area.css"))
        self.setObjectName("number-area")

        self.edit_line_num = parent

    def sizeHint(self):
        return QSize(self.edit_line_num.get_number_area_width(), 0)

    def paintEvent(self, event):
        self.edit_line_num.line_number_area_paint_event(event)
