import feedparser

url = feedparser.parse('https://www.tabnews.com.br/recentes/rss')
print(url.channel.title)

lenn = len(url.entries)

for i in range (1, lenn):
    print(f"\n{url.entries[i].title}\n")
    print(f"{url.entries[i].description}\n")
    print(f"{url.entries[i].link}")
