from rich import print
from rich.table import Table

table = Table(box=None)  # box=MINIMAL

table.add_column(style="on blue")

text = """
    [bold]Python OS[/bold]                         

    Type [b]pui[/b] to enter Python UI             

    For help please visit Python OS Github page    

    HAVE FUN!                                      
    The Python OS Developer                        

"""

for e, line in enumerate(text.splitlines()):
    if e == 3:
        table.add_row(line, style="on magenta")  # grey93
    else:
        table.add_row(line)

print(table)
