import requests
import re

from bs4 import BeautifulSoup

with open('example.mhtml', 'r') as example:
    soup = BeautifulSoup(example, 'html.parser')

news = soup.find_all('div', '3D"news_box"')

for _news in news:
    inner = _news.find('div', '3D"box_inner"')
    news_date = inner.find('div', '3D"date')
    try:
        news_date = news_date.string.lstrip()
        print(news_date)
    except AttributeError as e:
        print('Skipped, exception: ', e)

# print(len(soup.find_all('div', '3D"news_box"')))
# output: 9
