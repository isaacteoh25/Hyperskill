from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
# text = "We were on the Queen Elizabeth, coming back from our first trip to Europe."
text = input()

i = int(input())
print(regexp_tokenize((text), "[A-z]+")[i])
# ['I', 'have', 'got', 'a', 'cat', 'My', "cat's", 'name', 'is', 'C-3PO', "He's", 'golden']


text = "My favourite city is Lond0n."
print(regexp_tokenize((text), "[a-z]+"))