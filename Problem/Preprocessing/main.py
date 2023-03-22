
# str = input()
str = "Nobody expects the Spanish inquisition! And you?!"
# print(str.replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower())
print(str.lower().strip(",.!?!").replace("!", ""))