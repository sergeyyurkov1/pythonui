from textual.containers import Container, Horizontal
from textual.widgets import Static, Switch

import functions

Switch_Changed = Switch.Changed

layout = [
    Container(
        Horizontal(
            Static("Retro effects", classes="commands-static"),
            Switch(
                value=functions.read_yaml().get("retro_effects", False),
                name="retro_effects",
                classes="role-settings",
            ),
            classes="commands-horizontal",
        ),
        classes="commands-container",
    )
]
