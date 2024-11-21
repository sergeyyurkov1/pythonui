from textual.containers import Container, Horizontal
from textual.widgets import Static, Switch

Switch_Changed = Switch.Changed

layout = [
    Container(
        Horizontal(
            Static("Retro effects", classes="commands-static"),
            Switch(
                id="retro_effects",
                name="retro_effects",
                classes="role-settings",
            ),
            classes="commands-horizontal",
        ),
        classes="commands-container",
    )
]
