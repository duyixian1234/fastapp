from ..components import Page, H1, P, Button

Counter = Page()

count = 0

Counter.get("/")(
    lambda: (
        H1("Count Demo"),
        P(f"Count is set to {count}", id="count"),
        Button(
            "Increment",
            hx_post="/counter/increment",
            hx_target="#count",
            hx_swap="innerHTML",
        ),
    )
)


@Counter.post("/increment")
def increment():
    global count
    count += 1
    return f"Count is set to {count}"
