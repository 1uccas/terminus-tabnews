import feedparser
from rich.console import Console
from rich.table import Table
import webbrowser as web
import os
from time import sleep

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    table = Table()
    table.show_lines=True
    table.add_column("Item", justify="center")
    table.add_column("Titulo", justify="center")
    table.add_column("Descrição", justify="center")

    url = feedparser.parse('https://www.tabnews.com.br/recentes/rss')
    lenn = len(url.entries)

    for i in range (0, lenn):
        table.add_row(f"{i}",f"{url.entries[i].title}", f"{url.entries[i].description}")

    console.print(table)

    console.print("🎈 [yellow]Selecione um item[/yellow]\n[red][00] - Para SAIR (x)[/red]")
    try:
        number = (console.input("👉 ")).strip()

        if number.upper() == 'SAIR':
            console.print("🔓 [yellow]Saindo...[/yellow]")
            exit()
        elif int(number) < 0 or int(number) > int(lenn):
            console.print("👾 [bold][red]Error[/red][/bold] ~ [bold]Item não encontrado![/bold]")
            sleep(1)
            clear()
        else:
            console.print(f":warning-emoji: [purple]Abrindo[/purple] ~ [yellow]{url.entries[int(number)].title}[/yellow]")
            sleep(1)
            web.open(f"{url.entries[int(number)].link}")
            clear()
    except Exception as VE:
        console.print(f"👹 [red]Error[/red] ~ [pink]Valor não suportado[/pink]") 
        sleep(1)
        #clear()
