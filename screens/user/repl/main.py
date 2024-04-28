import io
import sys

from textual import on
from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button, Footer, Input, Log, TextArea


class Default(Screen):
    CSS_PATH = "main.tcss"

    BINDINGS = [("escape", "app.pop_screen", "Quit")]

    def compose(self) -> ComposeResult:
        yield Container(
            TextArea.code_editor(id="repl-input", tab_behavior="focus"),
            Container(Button("Evaluate", id="repl-evaluate"), classes="center-middle"),
            Log(id="repl-output"),
            id="repl",
        )
        yield Footer()

    @on(Button.Pressed, "#repl-evaluate")
    def handle_submit_repl(self, event: Input.Submitted) -> None:
        log = self.query_one("#repl-output")

        repl_input = self.query_one("#repl-input")

        cmd = repl_input.text

        if "os.system" in cmd:
            log.write_line("Please use 'subprocess.run' instead of 'os.system'.")
            log.write_line("\n")
            return

        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            exec(cmd)
            result = sys.stdout.getvalue()
            log.write_line(str(result))
            log.write_line("\n")
        except Exception as e:
            log.write_line(str(e))
            log.write_line("\n")

        sys.stdout = old_stdout
