from textual.app import ComposeResult, on
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button


class SignIn(Screen):
    DEFAULT_CSS = """
        SignIn {
            background: black;
        }
    """

    def compose(self) -> ComposeResult:
        self.button = Button("ENTER", id="open-loading")
        yield Container(self.button, classes="center-middle")

    def animate(self) -> None:
        self.button.styles.animate(
            "color",
            value="#22ef45",
            duration=1,
            final_value="black",
            on_complete=self.animate,
        )

    def on_mount(self) -> None:
        self.animate()

    @on(Button.Pressed, "#open-loading")
    def open_loading(self) -> None:
        self.app.pop_screen()
        self.app.push_screen("loading")
        self.app.uninstall_screen("signin")
