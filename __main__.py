import feedparser 

url = feedparser.parse('https://www.tabnews.com.br/recentes/rss')
print(url.feed.title)
