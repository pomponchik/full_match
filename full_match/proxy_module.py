import sys
from re import escape


class ProxyModule(sys.modules[__name__].__class__):  # type: ignore[misc]
    def __call__(self, string: str) -> str:
        return f'^{escape(string)}$'
