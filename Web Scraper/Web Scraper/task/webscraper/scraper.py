import json
import random
import re
import urllib
#
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
# # params = {'q': 'requests'}
# # r = requests.get('http://python.org/search', params=params)
# # print(r)
# i = 'https://www.imdb.com/title/tt10048342/'
# i = input()
# text = requests.get(i , headers={"accept-language": "en-US,en;q=0.9,uk;q=0.8,ru;q=0.7"})
# # soup = BeautifulSoup(text.content, 'html.parser')
# # url_input = url_input.split("/")
# a = dict()
# # if "quotes" in url_input and url.status_code == 200:
# if "imdb" not in i or "name" in i:
#     print("Invalid movie page!")
# elif text.status_code == 200:
#     try:
#         soup = BeautifulSoup(text.text, 'html.parser')
#         b = soup.find("div", class_="summary_text").contents[0].strip()
#         print(b)
#         # print(soup.prettify())
#         title = soup.find('title').contents[0]
#         a["title"]= title.split("(")[0].strip()
#         a["description"] =b
#
#         # print(text.json()['title'])
#         print(a)
#     except KeyError:
#         print('Invalid quote resource!')
# else:
#     print('Invalid quote resource!')
#
# import requests
# from bs4 import BeautifulSoup
#
# url = input()
# resp = requests.get(url, headers={"accept-language": "en-US,en;q=0.9,uk;q=0.8,ru;q=0.7"})
#
# if not resp:
#     content = 'Invalid movie page!'
# else:
#     html = BeautifulSoup(resp.content, 'html.parser')
#     title = html.select_one("div#star-rating-widget")
#     description = html.select_one("meta[name='description']")
#     if description and title:
#         content = {"title": title['data-title'], "description": description['content']}
#     else:
#         content = 'Invalid movie page!'
#
# print(content)
# db={}
# d = content.find('script', {'type': "application/ld+json"})
# d = str(d).replace('<script type="application/ld+json">', '').replace('</script>', '')
# d = json.loads(d)
# if d['@type'] == 'Movie' or d['@type'] == "TVSeries":
#     db['title'] = d['name']
#     disc = str(content.find('div', {'class': 'summary_text'}).text)
#     disc = disc.strip()
#     db['description'] = disc


# def request_quote():
#     r = requests.get(input("Input the URL:\n"))
#     try:
#         soup = BeautifulSoup(r.content, "lxml")
#         title = soup.find("h1").get_text(strip=True).partition("(")[0]
#         para = soup.find("div", "summary_text").get_text(strip=True)
#         print(json.dumps({"title": title, "description": para}))
#     except (KeyError, AttributeError):
#         print("Invalid movie page!")
#
#
# request_quote()
def request_quote():
    r = requests.get(input("Input the URL:\n"))
    try:
        soup = BeautifulSoup(r.content, "lxml")
        title = soup.find("h1").get_text(strip=True).partition("(")[0]
        para = soup.find("div", "summary_text").get_text(strip=True)
        print(json.dumps({"title": title, "description": para}))
    except (KeyError, AttributeError):
        print("Invalid movie page!")


def save_page_source():
    url = input("Input the URL:\n")
    r = requests.get(url)
    try:
        if not r:
            print(f"The URL returned {r.status_code}!")
            exit(0)
        with open('source.html', 'wb') as file:
            file.write(r.content)
    except:
        pass
    else:
        print("Content saved.")


save_page_source()
