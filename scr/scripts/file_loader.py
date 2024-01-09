from scr.exceptions import WrongFileExtension, NotFileError

import json
import os
from PIL import Image


class FileLoader:

    @staticmethod
    def __verify_file(__path: str, *__expansions: str) -> None:
        match __path:
            case path if not os.path.isfile(path):
                raise NotFileError(f"Argument must be a file, not directory ({path})")

            case path if not os.path.splitext(path)[1] in __expansions:
                raise WrongFileExtension(f"File extension must be in {__expansions}")

    @classmethod
    def load_style(cls, __path: str) -> str:
        cls.__verify_file(__path, ".css", ".qss")

        with open(os.path.normpath(__path), "r", encoding="utf-8") as file:
            result = file.read()

        return result

    @classmethod
    def load_json(cls, __path: str) -> str:
        cls.__verify_file(__path, ".json")

        with open(os.path.normpath(__path), "r", encoding="utf-8") as file:
            result = json.load(file)

        return result

    @classmethod
    def load_image(cls, __path) -> Image:
        cls.__verify_file(__path, ".png", ".jpg", ".jpeg")

        with Image.open(os.path.normpath(__path)) as image:
            result = image

        return result
