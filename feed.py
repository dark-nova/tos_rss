import datetime

from feedgen.feed import FeedGenerator

import scraper


def populate_item(fg: FeedGenerator, article: dict):
    """Populates an entry for `fg`.

    Args:
        fg (FeedGenerator): the feed to add entries
        article (dict): the article to enter as entry

    Returns:
        None
    
    """

    entry = fg.add_entry()
    entry.title(article['title'])
    entry.author({'name': 'Tree of Savior'})
    entry.description(article['title'])
    entry.link(href = article['url'])
    entry.guid(article['url'])
    entry.pubDate(article['date'])
    return


if __name__ == '__main__':
    fg = FeedGenerator()
    fg.title('Tree of Savior News')
    fg.author({'name': 'IMC Games'})
    fg.description('News for the International Tree of Savior Servers')
    fg.link(
        href='https://treeofsavior.com/page/news/',
        rel='alternate'
        )
    fg.link(
        href='https://dark-nova.me/tos/feed.xml',
        rel='self'
        )
    fg.logo('https://dark-nova.me/tos/feed.png')
    fg.language('en-US')

    all_news = scraper.get_news()
    for article in all_news:
        populate_item(fg, article)

    fg.rss_file('feed.xml')
