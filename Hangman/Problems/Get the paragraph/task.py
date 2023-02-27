import requests

from bs4 import BeautifulSoup

word = input()
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

res_p = soup.find_all('p')
for p in res_p:
    if word in p.text:
        print(p.text)
        break

import re
paragraphs = soup.find_all('p', text=re.compile(word))
for p in paragraphs:
    print(p.text + '\n')

