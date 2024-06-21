import feedparser
from rich.console import Console
from rich.table import Table

table = Table(title="Tabnews")
table.show_lines=True
table.add_column("title", justify="center")
table.add_column("link", justify="center")

url = feedparser.parse('https://www.tabnews.com.br/recentes/rss')
print(url.channel.title)

lenn = len(url.entries)

for i in range (1, lenn):
    print(f"\n{url.entries[i].title}\n")
    print(f"{url.entries[i].description}\n")
    print(f"{url.entries[i].link}")
