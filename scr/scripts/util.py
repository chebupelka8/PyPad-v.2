import os
import sys
import matplotlib.font_manager


def restart_application() -> None:
    os.execv(sys.executable, ['python'] + sys.argv)


def get_all_font_families() -> list[str]:
    return [f.name for f in matplotlib.font_manager.fontManager.ttflist]
