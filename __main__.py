import feedparser
from rich.console import Console
from rich.table import Table

table = Table(title="TabNews: Conteúdos para quem trabalha com Programação e Tecnologia")
table.show_lines=True
table.add_column("title", justify="center")
table.add_column("link", justify="center")

url = feedparser.parse('https://www.tabnews.com.br/recentes/rss')


lenn = len(url.entries)

for i in range (0, lenn):
    table.add_row(f"{url.entries[i].title}",f"{url.entries[i].link}")

console = Console()
console.print(table)