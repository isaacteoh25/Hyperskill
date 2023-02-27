
i = "lower camel case".split()
# i = input().split()
b =[]
for a in range(1, len(i)):
    b.append(i[a].capitalize())
# print(b)
print(i[0].lower() + ''.join(b))
word = str(input()).split()
print("".join([word[0]] + [x.title() for x in word[1:]]))