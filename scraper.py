from bs4 import BeautifulSoup
import requests

with open('example.mhtml', 'r') as example:
    soup = BeautifulSoup(example, 'html.parser')

for news in soup.find_all('div', '3D"news_box"'):
    #print(news)
    pass

# print(len(soup.find_all('div', '3D"news_box"')))
# output: 9
