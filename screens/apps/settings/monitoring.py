import random

from textual.containers import Center, Grid
from textual.widgets import Button, Sparkline

random.seed(73)
data = [random.expovariate(1 / 3) for _ in range(1000)]


layout = [
    Grid(
        Sparkline(data, summary_function=max),
        Sparkline(data, summary_function=max),
        Sparkline(data, summary_function=max),
        Sparkline(data, summary_function=max),
        # echo "CPU Usage: "$[100-$(vmstat 1 2|tail -1|awk '{print $15}')]"%"
        Center(
            Button(
                "Test",
                name="Test Button",
            ),
            id="monitoring-button-test-container",
        ),
    ),
]
