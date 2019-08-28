import logging
import re
import sqlite3

import pendulum
import requests
from bs4 import BeautifulSoup

import db


non_numbers = re.compile('[^0-9]')
no_quotes = re.compile('"')

months = {}
months[1] = re.compile('^jan', re.IGNORECASE)
months[2] = re.compile('^feb', re.IGNORECASE)
months[3] = re.compile('^mar', re.IGNORECASE)
months[4] = re.compile('^apr', re.IGNORECASE)
months[5] = re.compile('^may', re.IGNORECASE)
months[6] = re.compile('^jun', re.IGNORECASE)
months[7] = re.compile('^jul', re.IGNORECASE)
months[8] = re.compile('^aug', re.IGNORECASE)
months[9] = re.compile('^sep', re.IGNORECASE)
months[10] = re.compile('^oct', re.IGNORECASE)
months[11] = re.compile('^nov', re.IGNORECASE)
months[12] = re.compile('^dec', re.IGNORECASE)

# adapted from https://docs.python.org/3/howto/logging-cookbook.html
logger = logging.getLogger('tos_scraper')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('scraper.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


def convert_article_date(article_date: list):
    """Given a date in list like:
    ['January', '1st,', '2000']

    ...extract the date.

    Args:
        article_date (list): yes

    Returns:
        tuple: (year, month, day)

    """
    for m, regex in months.items():
        if regex.match(article_date[0]):
            month = m
    day = int(non_numbers.sub('', article_date[1]))
    year = int(article_date[2])
    return (year, month, day)


def get_article_url(article):
    """Gets the url of a given `article`.

    Args:
        article (bs4.element.Tag): the article in the page

    Returns:
        str: the url

    """
    url = no_quotes.sub('', article.a['href'])
    return f'https://treeofsavior.com{url}'


def get_news():
    # with open('example.html', 'r') as example:
    #     soup = BeautifulSoup(example, 'html.parser')
    page = requests.get('https://treeofsavior.com/page/news/')
    soup = BeautifulSoup(page.text, 'html.parser')

    news = soup.find_all('div', 'news_box')

    all_news = []

    for news_article in news:
        article = {}
        inner = news_article.find('div', 'box_inner')
        article_date = inner.find('div', 'date')
        try:
            article_date = article_date.string.lstrip().split()
            article['url'] = get_article_url(news_article)
            article['title'] = news_article.h3.string
            a_date = convert_article_date(article_date)
            today = pendulum.today()
            if db.check_if_entry_exists(article['url']):
                article['date'] = db.get_entry_time(article['url'])
            else:
                if today == pendulum.datetime(*a_date, tz = today.tz):
                    article['date'] = pendulum.datetime(
                        *a_date,
                        pendulum.now(tz = 'UTC').hour,
                        tz = 'UTC'
                        )
                else:
                    # If the article date doesn't match up with today's date,
                    # do not modify the publish time. Fallback for
                    # migrating setups, or resuming after pausing for some
                    # time.
                    article['date'] = pendulum.datetime(
                        *a_date,
                        0,
                        tz = 'UTC'
                        )
                db.add_entry(
                    article['url'],
                    pendulum.datetime(*article['date'])
                    )
            all_news.append(article)
        except AttributeError as e:
            logger.warning(
                f'Caught exception {e} from {article}, inner {inner}'
                )

    db.purge_old()

    return all_news
