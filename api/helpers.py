from fasthtml.common import Div, NotStr
from markdown import markdown

md_exts = "codehilite", "smarty", "extra", "sane_lists"


def Markdown(s, exts=md_exts, **kw):
    return Div(NotStr(markdown(s, extensions=exts)), **kw)
