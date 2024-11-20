import i3ipc
from i3ipc import Event

import functions


def main():
    def on_window_close(i3, e):
        tree = i3.get_tree()

        if len(tree.find_classed("terminal")) == 0:
            functions.log_to_txt("All terminal windows closed")

            i3.command(
                "exec xfce4-terminal --hide-menubar --hide-toolbar --hide-scrollbar"
            )

    i3 = i3ipc.Connection()

    i3.on(Event.WINDOW_CLOSE, on_window_close)


if __name__ == "__main__":
    main()