from scr.scripts import FileLoader, IconProvider
from scr.exceptions import NotDirectoryError

import os

from PySide6.QtWidgets import QTreeView, QFileSystemModel, QAbstractItemView


class FileTree(QTreeView):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/file_tree.css"))
        self.setObjectName("file-tree")
        self.setMinimumWidth(300)

        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)

        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.setModel(self.model)
        self.setRootIndex(self.model.index(""))
        self.setHeaderHidden(True)
        self.model.setIconProvider(IconProvider())

        for i in range(1, 4):
            self.header().setSectionHidden(i, True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()

        for url in urls:
            print(url)

    def get_path_by_index(self, __index) -> str:
        return self.model.filePath(__index)

    def get_file_icon(self, __index):
        return self.model.fileIcon(__index)

    def set_project_dir(self, __path: str):
        if not os.path.isdir(__path):
            raise NotDirectoryError("This must be a directory not file")

        self.model.setRootPath(__path)
        self.setRootIndex(self.model.index(__path))

    def open_file(self, __path: str) -> None:
        self.open_directory(os.path.dirname(__path))

    def open_directory(self, __path: str) -> None:
        self.model.setRootPath(__path)
        self.setRootIndex(self.model.index(__path))
