class CodeAnalyzer:

    @staticmethod
    def find_tabs_in_string(string: str, __cursor_index: int) -> int:
        res = 0

        for i, letter in enumerate(string):
            if letter == "\t" and i < __cursor_index:
                res += 1

            else:
                break

        return res

    @staticmethod
    def find_tabs_in_string_by_spaces(string, __cursor_index: int, __tab_count: int = 4) -> int:
        res = 0

        for i, letter in enumerate(string):
            if letter == " " and i < __cursor_index:
                res += 1

            else:
                break

        return res // __tab_count

    @staticmethod
    def check_last_character_is_colon(string: str) -> int:
        """This function returns 1 if the string ends with ':' else 0"""

        try:
            return 1 if string.rstrip()[-1] == ":" else 0
        except IndexError:
            return 0