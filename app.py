import glob
import importlib
import os
from importlib.machinery import SourceFileLoader

from textual.app import App

import clean
from functions import SettingsMixin, register_namespace
from screens.loading import Loading
from screens.main import Main
from screens.signin import SignIn

SCREENS_PATH = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "screens", "apps"
)
COMMANDS_PATH = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "screens", "commands"
)

TITLE = "PERSONAL TERMINAL"


class PersonalTerminal(App, SettingsMixin):
    ENABLE_COMMAND_PALETTE = False
    CSS_PATH = "app.tcss"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = TITLE

        self.user_screens = self.get_user_screens()
        self.user_subscreens = self.get_user_subscreens()
        self.user_commands = self.get_user_commands()

    # APPS
    @staticmethod
    def get_user_screens() -> list[str]:
        return sorted(
            [
                i
                for i in os.listdir(path=SCREENS_PATH)
                if not i.startswith("__")
                and not i.startswith("x_")
                and os.path.isdir(os.path.join(SCREENS_PATH, i))
            ]
        )

    # APP SCREENS
    @staticmethod
    def get_user_subscreens() -> list[str]:
        user_subscreens = []
        for i in glob.glob(os.path.join(SCREENS_PATH, "*", "screens", "*.py")):
            user_subscreens.append(i)

        return user_subscreens

    # COMMANDS
    @staticmethod
    def get_user_commands() -> list[str]:
        user_commands = []
        for i in glob.glob(os.path.join(COMMANDS_PATH, "*.py")):
            name = os.path.basename(i).split(".")[0]

            if name != "__init__":
                command_module = importlib.import_module(f"screens.commands.{name}")
                command = getattr(command_module, "default")

                user_commands.append(command)

        return user_commands

    def install_user_subscreens(self):
        for i in self.user_subscreens:
            name = os.path.basename(i).split(".")[0]

            subscreen = SourceFileLoader(name, i).load_module().Default

            self.install_screen(subscreen(id=name), name=name)

    def install_user_screens(self):
        for i in self.user_screens:
            screen_module = importlib.import_module(f"screens.apps.{i}.main")
            screen = getattr(screen_module, "Default")
            self.install_screen(screen(id=i), name=i)

            register_namespace(i)

    def push_user_screen(self, name):
        self.push_screen(name)

    def pop_user_screen(self, name):
        self.pop_screen(name)

    def on_mount(self) -> None:
        self.install_screen(SignIn(id="signin"), name="signin")
        self.install_screen(Loading(id="loading"), name="loading")
        self.install_screen(Main(id="main"), name="main")

        if self.search_key("disable_splashscreens") is False:
            self.push_screen("signin")
        else:
            self.push_screen("main")

        self.install_user_screens()


if __name__ == "__main__":
    clean.delete_folders()
    app = PersonalTerminal()
    app.run(mouse=True)
