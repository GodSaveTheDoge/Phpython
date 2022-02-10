# How this works:
#
# - Make a list of everyhing importable and expose it with __all__
# - Python fetches __all__ and tries to import everything
# - Via __getattr__ when the stuff starts getting imported by python, import
#   the required module and return it
# - Profit ???
import sys
import os

__all__ = [
    f.split(".", 1)[0]
    
    for spath in sys.path
    if os.path.exists(spath)

    for f in os.listdir(spath)
    if f.endswith(".py")
    or (
        os.path.isdir(os.path.join(spath,f))
        and os.path.exists(os.path.join(os.path.join(spath, f), "__init__.py"))
    )
]
__path__ = []

def __getattr__(name):
    try:
        return __import__(name)
    except Exception as e:
        return e
