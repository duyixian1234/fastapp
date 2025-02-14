from api.pages.home import HomePage
from fasthtml.common import serve
from .factory import app, rt


__all__ = ("app",)


rt("/")(HomePage)


if __name__ == "__main__":
    serve("api.index")
