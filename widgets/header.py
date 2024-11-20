from textual.widgets import Header


class PtHeader(Header):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_clock = True
        self.icon = "▮▮▮"
