import i3ipc
from i3ipc import Event

import functions


def main():
    # def on_window_new(i3, e):
    #     if e.container.name == "Terminal":
    #         functions.log_to_txt(e.container.name)
    #         # pyperclip.copy("~/pythonui/pos-greeter.py\n")
    #         # pyperclip.paste()

    def on_window_close(i3, e):
        tree = i3.get_tree()

        if len(tree.find_classed("Alacritty")) == 0:
            functions.log_to_txt("All terminal windows closed")

            i3.command("exec alacritty")

    i3 = i3ipc.Connection()

    i3.on(Event.WINDOW_CLOSE, on_window_close)
    # i3.on(Event.WINDOW_NEW, on_window_new)

    i3.main()


if __name__ == "__main__":
    main()
