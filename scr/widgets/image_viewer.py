from scr.scripts import FileLoader

from PySide6.QtWidgets import QLabel, QScrollArea, QApplication
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap


class ImageViewer(QScrollArea):
    def __init__(self, __path: str) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/image_viewer.css"))
        self.setObjectName("image-viewer")

        self.__image_view = QLabel()
        self.__image_view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pixmap = QPixmap(__path)
        self.__image_view.setPixmap(self.pixmap.scaled(self.pixmap.size(), Qt.AspectRatioMode.KeepAspectRatio))

        self.setWidget(self.__image_view)

        # vars
        self.size = self.pixmap.size()
        self.start_size = self.pixmap.size()

        self.iteration_zoom = [i for i in range(20, 300, 20)]
        self.current_zoom = self.iteration_zoom.index(100)

    def wheelEvent(self, arg__1) -> None:
        modifiers = QApplication.keyboardModifiers()

        if modifiers == Qt.ControlModifier:
            delta = arg__1.angleDelta().y()

            if delta > 0 and self.current_zoom < len(self.iteration_zoom) - 1:
                self.current_zoom += 1

            if delta < 0 and self.current_zoom > 0:
                self.current_zoom -= 1

            self.zoom(self.iteration_zoom[self.current_zoom])
        else:
            super().wheelEvent(arg__1)

    def zoom(self, delta: int) -> None:
        self.size.setWidth(self.start_size.width() * delta / 100)
        self.size.setHeight(self.start_size.height() * delta / 100)

        self.__image_view.resize(self.size)
        self.__image_view.setPixmap(self.pixmap.scaled(self.size, Qt.AspectRatioMode.KeepAspectRatio))
