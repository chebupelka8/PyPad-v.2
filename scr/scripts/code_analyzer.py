class CodeAnalyzer:

    @staticmethod
    def find_tabs_in_string(string: str) -> int:
        res = 0

        for letter in string:
            if letter == " ":
                res += 1
            else:
                break

        return res // 4

    @staticmethod
    def check_last_character_is_colon(string: str) -> int:
        """This function returns 1 if the string ends with ':' else 0"""

        try:
            return 1 if string.rstrip()[-1] == ":" else 0
        except IndexError:
            return 0