import os
import platform

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import HorizontalScroll
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input

TITLE = "PERSONAL TERMINAL"


class Main(Screen):
    CSS_PATH = "main.tcss"
    BINDINGS = [
        Binding(key="Tab", action="", description="Select a widget"),
        Binding(key="q", action="quit", description="Quit"),
    ]

    TITLE = TITLE

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app_ = app

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with HorizontalScroll(id="main-horizontalscroll"):
            for i in self.app_.user_screens:
                yield Button(
                    i.upper().replace("_", " ").replace("-", " "),
                    id=i,
                    classes="main-buttons",
                )
        yield Input(placeholder="Run a command", id="command")

        yield Footer()

    @on(Input.Submitted)
    def run_command(self):
        value = self.query_one("#command").value
        self.query_one("#command").clear()
        with self.app_.suspend():
            # TODO: check if running inside WSL: uname -a
            # $ startx /usr/bin/<> -- -br +bs -dpi 96
            # --mode 800x600
            if platform.system() == "Windows":
                os.system(
                    "cls && echo 'You are now in Terminal. Type <exit> or use <Ctrl+C> to return back to the UI.\n' && "
                    + value
                )
                os.system("cls")
            else:
                os.system(
                    "clear && echo 'You are now in Terminal. Type <exit> or use <Ctrl+C> to return back to the UI.\n' && "
                    + value
                )
                os.system("clear")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app_.push_user_screen(event.button.id)
