from ..components import Page, Markdown

Home = Page()

Home.get("/")(
    lambda: Markdown(
        """
A Simple Web App Built with FastHTML.

[Github Repo](https://github.com/duyixian1234/fastapp)
"""
    )
)
