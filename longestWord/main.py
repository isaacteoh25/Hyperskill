# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functools import reduce

# f = open("words_sequence.txt", "r")
f = open("text.txt", "r")
s = [y for x in f.readlines() for y in x.split()]
# longest = reduce(lambda x, y: y if len(x) < len(y) else x, s, "")
# print("The longest word is", longest, "and it is", len(longest),"characters long")

print(len(s))
