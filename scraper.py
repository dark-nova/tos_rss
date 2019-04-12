import requests
import re
import logging

from bs4 import BeautifulSoup


non_numbers = re.compile('[^0-9]')

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

with open('example.mhtml', 'r') as example:
    soup = BeautifulSoup(example, 'html.parser')

news = soup.find_all('div', '3D"news_box"')

for _news in news:
    inner = _news.find('div', '3D"box_inner"')
    news_date = inner.find('div', '3D"date')
    try:
        news_date = news_date.string.lstrip().split()
        #for month in months[1:]:
        print(news_date)
    except AttributeError as e:
        logger.warning('Caught exception {} from {}, inner {}'
                       .format(e, _news, inner))

# print(len(soup.find_all('div', '3D"news_box"')))
# output: 9
