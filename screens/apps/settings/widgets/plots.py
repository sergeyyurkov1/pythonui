from collections import deque

import psutil
from textual_plotext import PlotextPlot

n = 10


class CpuPlot(PlotextPlot):
    """A widget for plotting CPU load."""

    def __init__(
        self,
        title: str,
        *,
        name: str | None = None,
        id: str | None = None,  # pylint:disable=redefined-builtin
        classes: str | None = None,
        disabled: bool = False,
    ) -> None:
        """Initialise the CPU plot."""
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._title = title

    def on_mount(self) -> None:
        self.queue = deque([0] * n, maxlen=n)

        self.plt.plot(self.queue)  # xside=False, yside=False
        self.plt.title(self._title)
        self.plt.xticks(ticks=[])
        self.plt.yticks(ticks=[])
        self.plt.ylim(lower=0, upper=100)

    def update(self) -> None:
        self.queue.append(psutil.cpu_percent(interval=None))

        self.plt.clear_data()
        self.plt.plot(self.queue)
        self.refresh()


class RamPlot(PlotextPlot):
    """A widget for plotting RAM load."""

    def __init__(
        self,
        title: str,
        *,
        name: str | None = None,
        id: str | None = None,  # pylint:disable=redefined-builtin
        classes: str | None = None,
        disabled: bool = False,
    ) -> None:
        """Initialise the RAM plot."""
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._title = title

    def on_mount(self) -> None:
        self.percentages = [psutil.virtual_memory().percent]

        self.plt.bar([""], self.percentages, orientation="v", width=100)
        self.plt.title(self._title)
        self.plt.xticks(ticks=[])
        self.plt.yticks(ticks=[])
        self.plt.ylim(lower=0, upper=100)

    def update(self) -> None:
        self.percentages = [psutil.virtual_memory().percent]

        self.plt.clear_data()
        self.plt.bar([""], self.percentages, orientation="v", width=100)
        self.plt.xticks(ticks=[])
        self.plt.yticks(ticks=[])
        self.plt.ylim(lower=0, upper=100)

        self.refresh()


class DiskPlot(PlotextPlot):
    """A widget for plotting Disk load."""

    def __init__(
        self,
        title: str,
        *,
        name: str | None = None,
        id: str | None = None,  # pylint:disable=redefined-builtin
        classes: str | None = None,
        disabled: bool = False,
    ) -> None:
        """Initialise the Disk plot."""
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._title = title

    def on_mount(self) -> None:
        self.percentages = [psutil.disk_usage("/").percent]

        self.plt.bar([""], self.percentages, orientation="v", width=100)
        self.plt.title(self._title)
        self.plt.xticks(ticks=[])
        self.plt.yticks(ticks=[])
        self.plt.ylim(lower=0, upper=100)

    def update(self) -> None:
        self.percentages = [psutil.disk_usage("/").percent]

        self.plt.clear_data()
        self.plt.bar([""], self.percentages, orientation="v", width=100)
        self.plt.xticks(ticks=[])
        self.plt.yticks(ticks=[])
        self.plt.ylim(lower=0, upper=100)

        self.refresh()
