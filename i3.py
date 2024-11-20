import i3ipc
from i3ipc import Event

import functions


def on_window_close(i3, e):
    tree = i3.get_tree()

    print(len(tree.find_classed("Terminal")))

    if len(tree.find_classed("Terminal")) == 0:
        functions.log_to_txt("All terminal windows closed")


# def get_windows_on_ws(conn):
#     return filter(
#         lambda x: x.window, conn.get_tree().find_focused().workspace().descendents()
#     )


def main(args):
    i3 = i3ipc.Connection()

    i3.on(Event.WINDOW_CLOSE, on_window_close)


if __name__ == "__main__":
    main()
