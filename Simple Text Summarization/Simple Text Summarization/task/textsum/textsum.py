from lxml import etree
from bs4 import BeautifulSoup
from math import sqrt
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
root = etree.parse('news.xml').getroot()
soup = BeautifulSoup(etree.tostring(root), 'html.parser')

all_headers = soup.find_all('value', {'name': 'head'})
all_texts = soup.find_all('value', {'name': 'text'})

headers = []
for header in all_headers:
    headers.append(header.text)

texts = []
for txt in all_texts:
    texts.append(txt.text)

content_dict = {}
for idx, header in enumerate(headers):
    txt = texts[idx]
    tokens = sent_tokenize(txt)
    N = int(round(sqrt(len(tokens)), 0))
    content_dict[header] = tokens[:N]

for key, txt_ in content_dict.items():
    print('HEADER:', key)
    print('TEXT:', txt_[0])
    for txt in txt_[1:]:
        print(txt)
    print()