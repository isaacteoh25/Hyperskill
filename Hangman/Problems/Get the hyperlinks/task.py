import requests
from bs4 import BeautifulSoup

# 2
# index = int(input())
# file = input()

file = 'https://www.grammarly.com/blog/articles/'
# file = 'http://www.gutenberg.org/files/3825/3825-h/3825-h.htm'
r = requests.get(file)
# r = requests.get(paragraph)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
print(soup.head)
# a = soup.find_all('a')
# print(a[index].get('href'))
# print(a[2].get('href'))
# for i in a:
#     print(i.get('href'))
# paragraphs = soup.find_all('h2')
# print(paragraphs[1].text)
# for p in paragraphs:
#     print(p.text + '\n')
