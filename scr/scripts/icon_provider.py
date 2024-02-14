from PySide6.QtGui import QIcon, QAbstractFileIconProvider
from PySide6.QtWidgets import QFileIconProvider, QApplication, QStyle
from PySide6.QtCore import QFileInfo, QMimeDatabase

from scr.config import IconPaths


class IconProvider(QAbstractFileIconProvider):
    def icon(self, __info: QFileInfo):
        try:

            if __info.isDir():
                return QIcon(IconPaths.FolderIcons.DEFAULT)

            elif __info.isFile():
                if __info.suffix().lower() == "py":
                    return QIcon(IconPaths.FileIcons.PYTHON)

                elif __info.suffix().lower() in ("png", "jpg", "jpeg"):
                    return QIcon(IconPaths.FileIcons.PICTURE)

                elif __info.suffix().lower() in ("qss", "css"):
                    return QIcon(IconPaths.FileIcons.CSS)

                elif __info.suffix().lower() == "json":
                    return QIcon(IconPaths.FileIcons.JSON)

                elif __info.suffix().lower() == "txt":
                    return QIcon(IconPaths.FileIcons.TXT)

                elif __info.suffix().lower() == "java":
                    return QIcon(IconPaths.FileIcons.JAVA)

                elif __info.suffix().lower() == "html":
                    return QIcon(IconPaths.FileIcons.HTML)

                elif __info.suffix().lower() == "js":
                    return QIcon(IconPaths.FileIcons.JS)

                elif __info.suffix().lower() == "md":
                    return QIcon(IconPaths.FileIcons.README)

                else:
                    return QIcon(IconPaths.FileIcons.DEFAULT)

        except AttributeError:
            pass

        return super().icon(__info)


class FileIconProvider(QFileIconProvider):
    def icon(self, _input):
        if isinstance(_input, QFileInfo):
            if _input.isDir():
                return QApplication.style().standardIcon(QStyle.SP_DirIcon)
            elif _input.isFile():
                return QApplication.style().standardIcon(QStyle.SP_FileIcon)
        else:
            if _input == QAbstractFileIconProvider.Folder:
                return QApplication.style().standardIcon(QStyle.SP_DirIcon)
            elif _input == QAbstractFileIconProvider.File:
                return QApplication.style().standardIcon(QStyle.SP_FileIcon)
        return super().icon(_input)

class FIconProvider(QFileIconProvider):
    def __init__(self):
        super().__init__()
        self.mimeDatabase = QMimeDatabase()

    def icon(self, info: QFileInfo):
        if isinstance(info, QFileInfo):
            mimeType = self.mimeDatabase.mimeTypeForFile(info)
            return QIcon.fromTheme(mimeType.iconName())

        return super().icon(info)
