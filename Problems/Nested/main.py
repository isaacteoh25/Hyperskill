# please work with the variable children
children = {'Emily': 'artist', 'Adam': 'astronaut', 'Nancy': 'programmer'}
children['Emily']={'profession':'artist', 'age':5}
children['Adam']={'profession':'astronaut', 'age':9}
children['Nancy']={'profession':'programmer', 'age':14}
print(children)

ages = (5, 9, 14)
for (child, dream_job), age in zip(children.items(), ages):
    children[child] = {'profession': dream_job, 'age': age}

for (k, v), a in zip(children.items(), (5, 9, 14)):
    children[k] = {'profession': v, 'age': a}