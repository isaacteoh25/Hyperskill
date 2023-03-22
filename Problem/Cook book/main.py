pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
keys = ['pasta','apple pie','ratatouille','chocolate cake','omelette']
# keys = [pasta,apple_pie,ratatouille,chocolate_cake,omelette]
values = [pasta,apple_pie,ratatouille,chocolate_cake,omelette]
dic = dict(zip(keys, values))
b = input()
# for a in food:
#     if b in a:
#         print(a.replace("_", " ") + ' time!')
fl = []
for i in keys:
    if b in dic[i]:
        fl.append(i)
for j in fl:
    print(j+' time!')
