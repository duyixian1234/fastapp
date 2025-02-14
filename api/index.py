from fasthtml.common import *
from markdown import markdown

hdrs = (HighlightJS(langs=["python", "javascript", "html", "css"]),)

md_exts = "codehilite", "smarty", "extra", "sane_lists"


def Markdown(s, exts=md_exts, **kw):
    return Div(NotStr(markdown(s, extensions=exts)), **kw)


app, rt = fast_app(hdrs=hdrs)

content = """
Here are some _markdown_ elements.

- This is a list item
- This is another list item
- And this is a third list item

**Fenced code blocks work here.**
```python
def hello_world():
    print("Hello, world!")
```
"""


@rt("/")
def get(req):
    return Titled("Markdown rendering example", Markdown(content))


if __name__ == "__main__":
    serve()
