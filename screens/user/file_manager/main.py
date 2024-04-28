from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, LoadingIndicator


class Default(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Quit")]

    def compose(self) -> ComposeResult:
        yield LoadingIndicator()
        yield Footer()
