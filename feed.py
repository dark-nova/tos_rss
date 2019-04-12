import datetime 

from rfeed import *

import scraper


def populate_item(article):
    return Item(
        title = article['title'],
        link = article['url'],
        description = article['title'],
        author = 'Tree of Savior',
        guid = Guid(article['url']),
        pubDate = datetime.datetime(*article['date'])
    )


items = []

all_news = scraper.get_news()
for article in all_news:
    items.append(populate_item(article))

feed = Feed(
    title = "Tree of Savior News",
    link = "https://dark-nova.me/tos/feed.xml",
    description = "Tree of Savior News",
    language = "en-US",
    lastBuildDate = datetime.datetime.now(),
    items = items)

with open('/web/tos/feed.xml', 'w') as f:
    f.write(feed.rss())
