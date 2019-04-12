import requests
import re

from bs4 import BeautifulSoup


non_numbers = re.compile('[^0-9]')

months = []
months.append('0') # sentinel value
months.append(re.compile('^jan', re.IGNORECASE))
months.append(re.compile('^feb', re.IGNORECASE))
months.append(re.compile('^mar', re.IGNORECASE))
months.append(re.compile('^apr', re.IGNORECASE))
months.append(re.compile('^may', re.IGNORECASE))
months.append(re.compile('^jun', re.IGNORECASE))
months.append(re.compile('^jul', re.IGNORECASE))
months.append(re.compile('^aug', re.IGNORECASE))
months.append(re.compile('^sep', re.IGNORECASE))
months.append(re.compile('^oct', re.IGNORECASE))
months.append(re.compile('^nov', re.IGNORECASE))
months.append(re.compile('^dec', re.IGNORECASE))

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
