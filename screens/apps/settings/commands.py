from textual.containers import Container, Horizontal
from textual.widgets import Static, Switch

layout = [
    Container(
        Horizontal(
            Static("Retro effects", classes="commands-static"),
            Switch(animate=False),
            classes="commands-horizontal",
        ),
        classes="commands-container",
    )
]
