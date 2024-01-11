from scr.exceptions import WrongFileExtension, NotFileError

import os


class FileChecker:

    @staticmethod
    def verify_file_extensions(__path: str, *__extensions):
        match __path:
            case path if not os.path.isfile(path):
                raise NotFileError(f"Argument must be a file, not directory ({path})")

            case path if not os.path.splitext(path)[1] in __extensions:
                raise WrongFileExtension(f"File extension must be in {__extensions}")

    @classmethod
    def verify_python_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".py")

    @classmethod
    def verify_json_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".json")

    @classmethod
    def verify_style_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".css", ".qss")

    @classmethod
    def verify_text_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".txt", ".md", ".doc")
