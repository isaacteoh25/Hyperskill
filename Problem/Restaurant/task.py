import itertools

main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]
course = dict(zip(main_courses, price_main_courses))
dessert = dict(zip(desserts, price_desserts))
drink = dict(zip(drinks, price_drinks))
for k, v in course.items():
    for ke, ve in dessert.items():
        for key, val in drink.items():
            if (v + ve + val) <= 30:
                print(k+" " + ke + " " + key, v + ve + val)

from itertools import product

for course, dessert, drink in product(zip(main_courses, price_main_courses), zip(desserts, price_desserts),
                                      zip(drinks, price_drinks)):

    total_cost = course[1] + dessert[1] + drink[1]
    if total_cost <= 30:
        print(f'{course[0]} {dessert[0]} {drink[0]} {total_cost}')

for dishes, price in zip(itertools.product(main_courses, desserts, drinks), itertools.product(price_main_courses, price_desserts, price_drinks)):
    prices_all = sum(price)
    if prices_all <= 30:
        print(" ".join(dishes), prices_all)

for (course, course_price), (dessert, dessert_price), (drink, drink_price) \
        in itertools.product(zip(main_courses, price_main_courses),
                             zip(desserts, price_desserts),
                             zip(drinks, price_drinks)):
    if (course_price + dessert_price + drink_price) <= 30:
        print(course, dessert, drink, course_price + dessert_price + drink_price)

main = zip(main_courses, price_main_courses)
dess = zip(desserts, price_desserts)
drink = zip(drinks, price_drinks)
for nabor in itertools.product(main, dess, drink):
    s = nabor[0][1] + nabor[1][1] + nabor[2][1]
    if s <= 30:
        print(nabor[0][0], nabor[1][0], nabor[2][0], s)

for m, mp in zip(main_courses, price_main_courses):
    for d, dp in zip(desserts, price_desserts):
        for dr, drp in zip(drinks, price_drinks):
            if (mp + dp + drp) <= 30:
                temp = (mp + dp + drp)
                print(m, d, dr, temp)

dish_combinations = itertools.product(main_courses, desserts, drinks)
price_combinations = itertools.product(price_main_courses, price_desserts, price_drinks)
combo_list = [item for item in zip(dish_combinations, price_combinations)]
len_combo_list = len(combo_list)
for i in range(len_combo_list):
    if sum(combo_list[i][1]) <= 30:
        print(" ".join(combo_list[i][0]), sum(combo_list[i][1]))

for dishes, prices in zip(itertools.product(main_courses, desserts, drinks),
                          itertools.product(price_main_courses, price_desserts, price_drinks)):
    if sum(prices) <= 30:
        print(*dishes, sum(prices))

price_list = []
for x, y, z in itertools.product(price_main_courses, price_desserts, price_drinks):
    price_list.append(x + y + z)
food_list = []
a = itertools.product(main_courses, desserts, drinks)
for value in a:
    food_list.append(" ".join(value))
both = zip(food_list, price_list)
for value in both:
    if value[1] <= 30:
        print(' '.join(map(str, value)))

for i in product(main_courses, desserts, drinks):
    price = 0

    price += price_main_courses[main_courses.index(i[0])]
    price += price_desserts[desserts.index(i[1])]
    price += price_drinks[drinks.index(i[2])]

    if price <= 30:
        print(*i, price)