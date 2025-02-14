from fasthtml.common import Titled, Div, NotStr
from markdown import markdown


__all__ = "Titled", "Div", "NotStr", "Markdown"


def Markdown(s, exts=("codehilite", "smarty", "extra", "sane_lists"), **kw):
    return Div(NotStr(markdown(s, extensions=exts)), **kw)
