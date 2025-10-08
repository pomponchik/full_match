from re import escape


def match(string: str) -> str:
    return f'^{escape(string)}$'
