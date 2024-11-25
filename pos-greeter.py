from rich import box, print
from rich.table import Table

table = Table(box=box.MINIMAL)  # box=None, MINIMAL_DOUBLE_HEAD

table.add_column(style="on blue")  # style="magenta"

text = """
    [bold]Python OS[/bold]                      

    Type [b]pui[/b] to enter Python UI          

    For help please visit Python OS Github page 

    HAVE FUN!                                   
    The Python OS Developer                     

"""

for e, line in enumerate(text.splitlines()):
    if e == 3:
        table.add_row(line, style="on grey93")
    else:
        table.add_row(line)

print(table)
