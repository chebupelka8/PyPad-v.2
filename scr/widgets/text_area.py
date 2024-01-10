from scr.scripts import FileLoader

from PySide6.QtWidgets import QPlainTextEdit, QTextEdit, QWidget
from PySide6.QtGui import QColor, QTextFormat, QPainter, QFont
from PySide6.QtCore import Qt, QRect, QSize, QPoint


class TextEditorArea(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(FileLoader.load_style("scr/styles/text_area.css"))
        self.setObjectName("text-area")

        # self setup
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        # font setup
        self.__main_font = QFont("Cascadia mono", 18, 1, False)
        self.setFont(self.__main_font)

        # instances
        self.lineNumberArea = LineNumPaint(self)

        # connections
        self.__highlight_current_line()
        self.__update_line_number_area_width()
        self.blockCountChanged.connect(self.__update_line_number_area_width)
        self.cursorPositionChanged.connect(self.__update_current_line)
        self.cursorPositionChanged.connect(self.__highlight_current_line)
        self.textChanged.connect(self.__highlight_current_line())
        self.verticalScrollBar().valueChanged.connect(self.lineNumberArea.update)

        # variables
        self.__current_line = 0

    def wheelEvent(self, delta) -> None:
        self.lineNumberArea.update()
        super().wheelEvent(delta)

    def mousePressEvent(self, event) -> None:
        super().mousePressEvent(event)

        self.update()
        self.lineNumberArea.update()
        self.__highlight_current_line()

    def keyPressEvent(self, event):
        self.lineNumberArea.update()

        super().keyPressEvent(event)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        content_rect = self.contentsRect()
        self.lineNumberArea.setGeometry(
            QRect(content_rect.left(), content_rect.top(), self.get_number_area_width(), content_rect.height())
        )

    def get_current_line(self) -> int:
        return self.__current_line

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
        painter = QPainter(self.lineNumberArea)

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
                painter.setFont(self.__main_font)
                painter.setPen(QColor("#b3b3b3"))

                painter.drawText(0, top, self.lineNumberArea.width(), height, Qt.AlignCenter, number)

            block = block.next()
            top = top + line_height
            block_number += 1


class LineNumPaint(QWidget):
    def __init__(self, parent: TextEditorArea):
        super().__init__(parent)

        self.setObjectName("number-area")

        self.edit_line_num = parent

    def sizeHint(self):
        return QSize(self.edit_line_num.get_number_area_width(), 0)

    def paintEvent(self, event):
        self.edit_line_num.line_number_area_paint_event(event)
