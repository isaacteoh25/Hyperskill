from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize
text = input()
num = int(input())
# print(sent_tokenize(text))
t = sent_tokenize(text)
print(regexp_tokenize(t[num], "[A-z']+"))