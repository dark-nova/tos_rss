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

# feed = Feed(
#     title = "Sample RSS Feed",
#     link = "http://www.example.com/rss",
#     description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
#     language = "en-US",
#     lastBuildDate = datetime.datetime.now(),
#     items = [item1, item2])

# print(feed.rss())
