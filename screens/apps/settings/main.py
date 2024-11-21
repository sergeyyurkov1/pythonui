import random

from textual import on
from textual.app import ComposeResult
from textual.containers import Container, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, ContentSwitcher, Footer, Header, Static

import functions

# from widgets.header import PtHeader
from .about import layout as about_layout
from .commands import Switch_Changed
from .commands import layout as commands_layout
from .monitoring import layout as monitoring_layout

random.seed(73)

LAYOUT = {
    "About": about_layout,
    "Monitoring": monitoring_layout,
    "Commands": commands_layout,
    # "Test": [],
}


class Default(Screen, functions.SettingsMixin):
    CSS_PATH = "main.tcss"

    BINDINGS = [("escape", "app.pop_screen", "Close")]

    def compose(self) -> ComposeResult:
        # yield PtHeader()
        yield Header(show_clock=True, icon="▮▮▮")

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
                            classes="role-contentswitcher settings-buttons",  # "role-" widget classes are not for styling, they are handler function selectors
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

    @on(Button.Pressed, ".role-contentswitcher")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id
        self.sub_title = str(event.button.label).upper()

    @on(Switch_Changed, ".role-settings")
    def handle_switch_change(self, event):
        self.write_settings(event.switch.name, event.switch.value)

        # self.notify("Saved.")

    def on_mount(self) -> None:
        # self.sub_title = self.namespace.upper().replace("_", " ").replace("-", " ")
        self.query_one("#retro_effects").value = self.read_settings("retro_effects")
        self.set_interval(2, self.update_plots)

    def update_plots(self) -> None:
        for plot in self.query(".role-plotextplot"):
            plot.update()
