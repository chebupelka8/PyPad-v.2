from scr.scripts import FileLoader

import os

from PySide6.QtWidgets import QTreeView, QFileSystemModel


class FileTree(QTreeView):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/file_tree.css"))
        self.setObjectName("file-tree")

        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.setModel(self.model)
        self.setRootIndex(self.model.index(""))
        self.setHeaderHidden(True)

        for i in range(1, 4): self.header().setSectionHidden(i, True)

    def open_file(self, __path: str) -> None:
        if not os.path.isfile(__path):
            print("Must be a file")

        self.open_directory(os.path.dirname(__path))

    def open_directory(self, __path: str) -> None:
        if not os.path.isdir(__path):
            print("Must be a dir")

        try:
            self.model.setRootPath(__path)
            self.setRootIndex(self.model.index(__path))
        except FileNotFoundError:
            print("File not found")
