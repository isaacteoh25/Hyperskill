# put your python code here
import string
# put your python code here

keys = []
values = []

for key in string.ascii_lowercase:
    keys.append(key)

for value in string.ascii_lowercase:
    value = value * 2
    values.append(value)

double_alphabet = dict(zip(keys, values))

# double_alphabet = {}
# for i in range(ord('a'), ord('z') + 1):
#     double_alphabet[chr(i)] = chr(i) + chr(i)

# from string import ascii_lowercase as letters
# double_alphabet = {a: a * 2 for a in letters}

# double_alphabet = {chr(character): chr(character) * 2 for character in range(97, 123)}

# from string import ascii_lowercase
# double_alphabet = {}
# for letter in ascii_lowercase:
#     double_alphabet[letter] = letter * 2

# double_alphabet = {x: x * 2 for x in 'qwertyuiopasdfghjklzxcvbnm'}