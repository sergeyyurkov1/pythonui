from textual.containers import Grid

from .widgets.plots import CpuPlot, DiskPlot, RamPlot

layout = [
    Grid(
        CpuPlot(title="CPU", classes="role-plotextplot"),
        RamPlot(title="RAM", classes="role-plotextplot"),
        DiskPlot(title="Disk", classes="role-plotextplot"),
        # PlotextPlot(classes="role-plotextplot", name=""),
        # echo "CPU Usage: "$[100-$(vmstat 1 2|tail -1|awk '{print $15}')]"%"
        # Center(
        #     Button(
        #         "Test",
        #         name="Test Button",
        #     ),
        #     id="monitoring-button-test-container",
        # ),
    ),
]
