from fasthtml.common import Titled
from ..helpers import Markdown

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


HomePage = lambda: Titled("Markdown rendering example", Markdown(content))
