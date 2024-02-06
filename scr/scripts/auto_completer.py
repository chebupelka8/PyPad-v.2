from jedi import Script
from PySide6.QtCore import QRunnable, QObject, Slot, Signal, QThreadPool


class CompleterSignal(QObject):
    res = Signal(list)


class AutoCompleter(QRunnable):
    def __init__(self, __path: str, __text: str) -> None:
        super().__init__()

        self.__path = __path
        self.__text = __text
        self.signal = CompleterSignal()

        self.__completions = []

    def get_completions(self, __text: str) -> list[str] | None:
        if __text.strip("\n").strip(" ") == "": return

        script = Script(__text, path=self.__path)
        completions = script.complete()
        res = [i.name for i in completions]

        return res

    def get(self):
        return self.__completions

    @Slot()
    def run(self):
        self.__completions = self.get_completions(self.__text)
        # print(self.__completions)
        self.signal.res.emit(self.__completions)
