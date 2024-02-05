from jedi import Script
from PySide6.QtCore import QThread


class Completer:
    def __init__(self, __path: str):

        self.__text = None
        self.__path = __path

        self.__completions = []

    def get_completions(self, __text: str) -> list[str] | None:
        self.__text = __text
        if self.__text.strip("\n").strip(" ") == "": return

        script = Script(__text, path=self.__path)
        completions = script.complete()
        res = [i.name for i in completions]
        self.__completions = res

        return res

    def get(self) -> list[str]:
        return self.__completions

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, __text):
        self.__text = __text


class AutoCompleter(QThread):
    def __init__(self, __path: str):
        super().__init__()

        self.__completer = Completer(__path)

    def get(self) -> list[str]:
        return self.__completer.get()

    def run(self):
        self.__completer.get_completions(self.__completer.text)

        self.finished.emit()

    def st(self, __text: str):
        self.__completer.text = __text

        # self.quit()
        self.start()
