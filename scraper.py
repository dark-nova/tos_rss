from bs4 import BeautifulSoup
import requests

with open('example.mhtml', 'r') as example_file:
    example = example_file.read()

soup = BeautifulSoup(example, 'html.parser')

for news in soup.find_all('div', '3D"news_box"'):
    #print(news)
    pass