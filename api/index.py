from fasthtml.common import serve

from .factory import app, rt
from .layout import Layout
from .pages.counter import Counter
from .pages.home import Home

rt("/")(Layout)
app.mount("/home", Home)
app.mount("/counter", Counter)


if __name__ == "__main__":
    serve("api.index")
