import sys

from full_match.proxy_module import ProxyModule as ProxyModule


sys.modules[__name__].__class__ = ProxyModule
