import requests
import re
import logging

from bs4 import BeautifulSoup


non_numbers = re.compile('[^0-9]')
no_3D = re.compile('3D')
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


def convert_article_date(article_date):
    for _m, regex in months.items():
        if regex.match(article_date[0]):
            month = _m
    day = int(non_numbers.sub('', article_date[1]))
    year = int(article_date[2])
    return (year, month, day)


def get_article_url(article):
    url = article.a['href']
    url = no_3D.sub('', url)
    url = no_quotes.sub('', url)
    return url


def get_news():
    with open('example.mhtml', 'r') as example:
        soup = BeautifulSoup(example, 'html.parser')

    news = soup.find_all('div', '3D"news_box"')

    all_news = []

    for news_article in news:
        article = {}
        inner = news_article.find('div', '3D"box_inner"')
        article_date = inner.find('div', '3D"date')
        try:
            article_date = article_date.string.lstrip().split()
            article['date'] = convert_article_date(article_date)
            article['url'] = get_article_url(news_article)
            article['title'] = news_article.h3.string
            all_news.append(article)
        except AttributeError as e:
            logger.warning('Caught exception {} from {}, inner {}'
                           .format(e, article, inner))
            pass

    return all_news

# print(len(soup.find_all('div', '3D"news_box"')))
# output: 9
