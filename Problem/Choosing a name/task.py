import itertools


first_names = ['Anna', 'Catarina']
middle_names = ['Luisa', 'Maria']
for first, second in itertools.product(first_names, middle_names) :
    print(first, second)
    for name in itertools.product(first_names, middle_names):
        print(*name)
        print(' '.join(name))
[print(x, y) for x, y in itertools.product(first_names, middle_names)]