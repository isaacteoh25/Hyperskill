from lxml import etree
file_name = "news.xml"
root = etree.parse(file_name).getroot()

dic = {}

data = root[0]
for oneData in data:
    dic[oneData[0].text] = oneData[1].text

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import nltk
from collections import Counter


lemm = WordNetLemmatizer()

punct = list(string.punctuation)

answer = {}
for title, corpus in dic.items():
    tokens = word_tokenize(corpus.lower())
    lemms = [lemm.lemmatize(word) for word in tokens]
    lemms = [word for word in lemms if word not in list(string.punctuation)]
    lemms = [word for word in lemms if word not in stopwords.words('english')]
    lemms = [nltk.pos_tag([word]) for word in lemms]
    lemms = [lst[0] for lst in lemms]
    lemms = [word for word, tag in lemms if tag == 'NN']

    most_common = Counter(lemms).most_common(20)
    answer[title] = list(most_common)

def customSort(lst):
    dic = {}

    for item in lst:
        dic.setdefault(item[1], []).append(item[0])

    indices = sorted(list(dic.keys()), reverse=True)

    final = []
    for index in indices:
        vals = dic[index]
        if len(vals) == 1:
            final += vals

        else:
            vals = sorted(vals, reverse=True)
            final += vals

    return final


for title in answer:
    print(f"{title}:")
    reverse_list = customSort(answer[title])
    print(*reverse_list[:5], end="\n\n")