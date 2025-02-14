from ..components import Titled, Markdown

HomePage = lambda: Titled("Fast App", Markdown(content))

content = """
Here are some _markdown_ elements.

- This is a list item
- This is another list item
- And this is a third list item

This is a table.

| Tables        | Are           | Cool  |
| ------------ |:-------------:| -----:|
| col 3 is     | right-aligned | $1600 |
| col 2 is     | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

**Fenced code blocks work here.**
```python
def hello_world():
    print("Hello, world!")
```
"""
