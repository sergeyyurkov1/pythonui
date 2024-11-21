import glob
import os
import pathlib

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, HorizontalScroll
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, Footer, Header, Input

import functions

# from widgets.header import PtHeader

BIN_PATHS = [r"/usr/bin"]


class Launcher(ModalScreen[str]):
    BINDINGS = [
        Binding(key="escape", action="app.pop_screen"),
        Binding(key="f9", action="sync"),
    ]

    DEFAULT_CSS = """
        Launcher {
            align: center middle;
            layout: vertical;

            & > Button {
                width: 50%;
            }
        }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bins = self.get_bins(BIN_PATHS)

    def action_sync(self):
        with self.app.batch_update():
            self.query(Button).remove()
            buttons = [Button(i["name"], name=i["path"]) for i in self.bins]
            self.mount_all(buttons)

    def on_mount(self) -> None:
        print(self.bins)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.name)

    @staticmethod
    def get_bins(paths: list) -> list[dict]:
        bins = []
        for path in paths:
            for p in glob.glob(os.path.join(path, "*")):
                if not pathlib.Path(p).is_symlink():
                    name = os.path.basename(p)  # .split(".")[0]
                    bins.append({"name": name, "path": p})

        return sorted(bins, key=lambda x: x["name"])

    def compose(self) -> ComposeResult:
        for i in self.bins:
            yield Button(i["name"], name=i["path"])


class Main(Screen, functions.SettingsMixin):
    CSS_PATH = "main.tcss"

    BINDINGS = [
        Binding(key="tab", action="app.focus_next", description="Select a widget"),
        Binding(key="f3", action="open_launcher", description="Open Launcher"),
        Binding(key="q", action="app.quit", description="Quit"),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        # yield PtHeader()
        yield Header(show_clock=True, icon="▮▮▮")

        with HorizontalScroll(id="main-horizontalscroll"):
            for i in self.app.user_screens:
                yield Container(
                    Button(
                        i.upper().replace("_", " ").replace("-", " "),
                        id=i,
                        classes="main-buttons",
                        name="screens",
                    ),
                    classes="main-container-buttons",
                    id=f"main-button-{i}",
                )
            for e, i in enumerate(self.app.user_commands):
                yield Container(
                    Button(
                        i["name"].upper().replace("_", " ").replace("-", " "),
                        id=f"command-{e}",
                        classes="main-buttons",
                        name=i["command"],
                        tooltip=i["tooltip"],
                    ),
                    classes="main-container-buttons",
                    id=f"main-button-{e}",
                )
        yield Input(placeholder="Run a command", id="command", classes="main-input")

        yield Footer()

    # =================================================================================
    def action_open_launcher(self) -> None:
        self.app.push_screen(Launcher(), self.run_command)

    @on(Input.Submitted)
    def handle_input_submitted(self, event: Input.Submitted):
        command = self.query_one("#command").value
        self.query_one("#command").clear()

        self.run_command(command=command)

        self.query(".main-buttons").first().focus()
        self.query_one("#command").focus()

    def run_command(self, command) -> None:
        # retro_effects = self.read_settings("retro_effects", "settings")
        retro_effects = self.search_key("retro_effects")

        functions.log_to_txt(f"Run '{command}', retro_effects: {retro_effects}")

        with self.app.suspend():
            # xinit -geometry =640x480+0+0 -fn 8x13 -j -fg white -bg black /usr/bin/<>
            # TODO: check if running inside WSL: uname -a
            # $ startx /usr/bin/<> -- -br +bs -dpi 96
            # --mode 800x600
            if retro_effects:
                command = f'cool-retro-term --profile "Futuristic" -e {command}'
            command = f"clear && echo 'You are now in Terminal. Type <exit> ( <exit()> if in REPL ) or use <Ctrl+C> to return back to the UI.\n\nPlease wait...\n' && {command}"
            os.system(command)
            os.system("clear")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.name == "screens":
            self.app.push_user_screen(event.button.id)

        if "command" in event.button.id:
            self.run_command(event.button.name)
            self.query(".main-buttons").first().focus()
            self.query_one(f"#{event.button.id}").focus()
