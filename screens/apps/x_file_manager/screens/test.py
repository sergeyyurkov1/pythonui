from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import LoadingIndicator


class Default(ModalScreen):
    def compose(self) -> ComposeResult:
        yield LoadingIndicator()
