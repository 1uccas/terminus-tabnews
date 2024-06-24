import feedparser
from rich.console import Console
from rich.table import Table
import webbrowser as web

console = Console()

table = Table(title="TabNews: Conteúdos para quem trabalha com Programação e Tecnologia")
table.show_lines=True
table.add_column("Item", justify="center")
table.add_column("title", justify="center")
table.add_column("link", justify="center")

url = feedparser.parse('https://www.tabnews.com.br/recentes/rss')
lenn = len(url.entries)

for i in range (0, lenn):
    table.add_row(f"{i}",f"{url.entries[i].title}",f"{url.entries[i].link}")

console.print(table)

console.print("[green]Deseja abrir qual opção?[/green]")
while True:
    try:
        number = int(console.input("[green]~>[/green]"))
        if number < 0 or number > lenn:
            console.print("[red]Error ~ Valor superior/inferior ao apresentado[/red]")
        else:

            web.open(f"{url.entries[number].link}")
            break
    except ValueError as VE:
        console.print("[yellow]Error ~ Valor não suportado[/yellow]") 
