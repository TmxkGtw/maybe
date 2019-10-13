from typing import Callable

class Fn:
    def __init__(self, action : Callable, *args, **kwargs):
        self.process = lambda : action(*args, **kwargs)

    def __call__(self):
        return self.process()

class Maybe:
    def __init__(self, value, condition : bool = True):
        self.value     = value
        self.condition = condition

    def __call__(self):
        if not self.condition:
            return None
        elif callable(self.value):
            return self.value()
        else:
            return self.value

    def __or__(self, other : "Maybe"):
        if self.condition:
            return self.__call__()
        elif other.condition:
            return other.__call__()
        else:
            return other

# Aliases
maybe = Maybe
fn    = Fn