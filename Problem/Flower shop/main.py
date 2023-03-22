from itertools import combinations, chain, product

flower_names = ['rose', 'tulip', 'sunflower', 'daisy']


it = chain(combinations(flower_names, 1), combinations(flower_names, 2), combinations(flower_names, 3))
for i in it:
    print(i)


main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

for m, de, dr in product(zip(main_courses, price_main_courses), zip(desserts, price_desserts), zip(drinks, price_drinks)):
    if m[1] + de[1] + dr[1] <= 30:
        print(m[0], de[0], dr[0], m[1] + de[1] + dr[1])

