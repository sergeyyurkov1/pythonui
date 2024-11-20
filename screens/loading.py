from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Label, ProgressBar

# from screens.widgets.spinner import SpinnerWidget

label1 = r"""
   _____ _   _____    __ __ ________    _____   ____ __
  / ___// | / /   |  / //_// ____/ /   /  _/ | / / //_/
  \__ \/  |/ / /| | / ,<  / __/ / /    / //  |/ / ,<   
 ___/ / /|  / ___ |/ /| |/ /___/ /____/ // /|  / /| |  
/____/_/ |_/_/  |_/_/ |_/_____/_____/___/_/ |_/_/ |_|  

                                    A SNAKEWARE PROJECT
"""

label2 = "A SNAKEWARE PROJECT"

label3 = "(C) SY-LINK DATA SYSTEMS"


class Loading(Screen):
    CSS = """
        SpinnerWidget {
            content-align: center middle;
        }

        Loading {
            background: black;
        }

        Bar > .bar--complete {
            color: #22ef45;
        }
    """

    def compose(self) -> ComposeResult:
        yield Container(
            Container(
                Container(Label(label1), id="label1"),
                Container(ProgressBar(total=100), id="progressbar"),
                # Container(SpinnerWidget(), id="progressbar"),
                Container(Label(label3), id="label3"),
                classes="center-middle",
                id="container",
            ),
            classes="center-middle",
        )

    def on_mount(self) -> None:
        self.timer = self.set_interval(1, self.progressbar_handler)

    def progressbar_handler(self) -> None:
        pb = self.query_one(ProgressBar)
        if pb.progress < 100:
            pb.advance(25)
        else:  # open Main
            self.timer.stop()
            self.app.pop_screen()
            self.app.push_screen("main")
            self.app.uninstall_screen("loading")
