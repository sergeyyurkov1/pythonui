import platform
import subprocess

from textual import on
from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Footer, Input, Log


class Default(Screen):
    CSS_PATH = "main.tcss"

    BINDINGS = [("escape", "app.pop_screen", "Quit")]

    def compose(self) -> ComposeResult:
        if platform.system() == "Windows":
            placeholder = "> "
        else:
            placeholder = "$ "

        yield Container(
            Input(placeholder=placeholder, id="terminal-input"),
            Log(id="terminal-output"),
        )

        yield Footer()

    @on(Input.Submitted, "#terminal-input")
    def handle_submit_terminal(self, event: Input.Submitted) -> None:
        self.query_one("#terminal-input").clear()

        log = self.query_one("#terminal-output")

        result = subprocess.run(
            [event.value], shell=True, capture_output=True, text=True
        )

        log.write_line(str(result.stdout))
        log.write_line(str(result.stderr))
        log.write_line("\n")
