from rich import box, print
from rich.table import Table

table = Table(box=box.MINIMAL)

table.add_column(style="on blue")

text = """
    [bold]Python OS[/bold]                         

    Type [b]pui[/b] to enter Python UI             

    For help please visit Python OS Github page    

    HAVE FUN!                                      
    The Python OS Developer                        

"""

for line in text.splitlines():
    table.add_row(line)

print(table)
print("\n")
