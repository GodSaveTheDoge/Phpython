# How this works:
#
# - Make a list of everyhing importable and expose it with __all__
# - Python fetches __all__ and tries to import everything
# - Via __getattr__ when the stuff starts getting imported by python, import
#   the required module and return it
# - Profit ???
import sys
import os

mods = [
    [
        f.split(".", 1)[0]
        for f in os.listdir(spath)
        if f.endswith(".py")
        or (
            os.path.isdir(f)
            and os.path.exists(os.path.join(f, "__init__.p__init__.py"))
        )
    ]
    for spath in sys.path
    if os.path.exists(spath)
]
__all__ = [f for m in mods for f in m]
__path__ = []

def __getattr__(name):
    return __import__(name)
