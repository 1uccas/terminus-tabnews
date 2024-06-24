import feedparser
from rich.console import Console
from rich.table import Table
import webbrowser as web

console = Console()

table = Table()
table.show_lines=True
table.add_column("Item", justify="center")
table.add_column("title", justify="center")
table.add_column("link", justify="center")

url = feedparser.parse('https://www.tabnews.com.br/recentes/rss')
lenn = len(url.entries)

for i in range (0, lenn):
    table.add_row(f"{i}",f"{url.entries[i].title}",f"{url.entries[i].link}")

console.print(table)

console.print("🎈 [yellow]Selecione um item[/yellow]")
while True:
    try:
        number = int(console.input("👉 "))
        if number < 0 or number > lenn:
            console.print("👾 [bold][red]Error[/red][/bold] ~ [bold]Valor superior/inferior ao apresentado[/bold]")
        else:
            console.print(f":warning-emoji: [purple]Abrindo[/purple] ~ [yellow]{url.entries[number].title}[/yellow]")
            web.open(f"{url.entries[number].link}")
            break
    except ValueError as VE:
        console.print("👹 [red]Error[/red] ~ [pink]Valor não suportado[/pink]") 
