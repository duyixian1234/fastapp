from fasthtml.common import (
    Div,
    Nav,
    NotStr,
    Titled,
    A,
    Main,
    FastHTML as Page,
    H1,
    P,
    Button,
    Header,
)
from markdown import markdown

__all__ = (
    "Titled",
    "Div",
    "NotStr",
    "Markdown",
    "Nav",
    "A",
    "Main",
    "Page",
    "H1",
    "P",
    "Button",
    "Header",
)


def Markdown(s, exts=("codehilite", "smarty", "extra", "sane_lists"), **kw):
    return Div(NotStr(markdown(s, extensions=exts)), **kw)
