# from textual import events
from textual.app import ComposeResult
from textual.containers import Container, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, ContentSwitcher, Footer, Header, Static

import functions

from .about import layout as about_layout
from .commands import layout as commands_layout
from .monitoring import layout as monitoring_layout

LAYOUT = {
    "About": about_layout,
    "Monitoring": monitoring_layout,
    "Commands": commands_layout,
}


class Default(Screen):
    CSS_PATH = "main.tcss"

    BINDINGS = [("escape", "app.pop_screen", "Close")]

    # def action_set_background(self, color: str) -> None:
    #     self.screen.styles.background = color

    # async def on_key(self, event: events.Key) -> None:
    #     if event.key == "r":
    #         await self.run_action("set_background('red')")

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True, icon="")

        with Container(id="col1"):
            with Container():
                yield Static(
                    self.id.upper().replace("_", " ").replace("-", " "), id="title"
                )
            with VerticalScroll(id="settings-buttons"):
                for k, _ in LAYOUT.items():
                    with Container(classes="settings-button-container"):
                        yield Button(
                            k,
                            id=f"settings-buttons-{k.lower().replace(' ', '-')}",
                            classes="settings-buttons",
                            name="tabs",
                        )

        initial = list(LAYOUT.keys())[0].lower().replace(" ", "-")
        with ContentSwitcher(
            initial=f"settings-buttons-{initial}", id="settings-contentswitcher"
        ):
            for k, v in LAYOUT.items():
                with VerticalScroll(
                    id=f"settings-buttons-{k.lower().replace(' ', '-')}",
                ):
                    for i in v:
                        yield i

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.name == "tabs":
            self.query_one(ContentSwitcher).current = event.button.id
        else:
            self.notify(event.button.name)

    def on_switch_changed(self, event):
        config = functions.read_yaml() or {}
        config["retro_effects"] = event.switch.value
        functions.write_yaml(config)

        self.notify("Saved.")
