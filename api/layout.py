from .components import A, Main, Nav, Titled, Header

Layout = lambda: Titled(
    "Fast App",
    Header(
        *tuple(
            map(
                lambda page: Nav(
                    A(page, hx_get=f"/{page}", hx_target="#main", hx_swap="innerHTML")
                ),
                ["home", "counter"],
            )
        ),
        cls="grid",
    ),
    Main(id="main", hx_get="/home", hx_trigger="load", cls="container-fluid"),
)
