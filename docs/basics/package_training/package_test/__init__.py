from .module_1 import *       # also constrained by __all__'s
from .module_2 import *       # in the __init__.py's


__all__ = ['foo1', 'bar1']   # further constraining the names advertised
#