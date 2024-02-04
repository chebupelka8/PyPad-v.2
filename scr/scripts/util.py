import os
import sys


def restart_application() -> None:
    os.execv(sys.executable, ['python'] + sys.argv)