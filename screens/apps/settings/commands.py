from textual.containers import Container, Horizontal
from textual.widgets import Static, Switch

import functions

layout = [
    Container(
        Horizontal(
            Static("Retro effects", classes="commands-static"),
            Switch(
                value=functions.read_yaml().get("retro_effects", False), animate=False
            ),
            classes="commands-horizontal",
        ),
        classes="commands-container",
    )
]
