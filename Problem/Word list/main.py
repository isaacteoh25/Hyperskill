text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
x = int(input())
y = [name for names in text for name in names if len(name) <= x ]
print(y)


country_list = [["Moscow", "Cheboksary", "Sochi"], ["Paris", "Lyon", "Nice"],
                ["New York", "Dallas", "San Francisco"]]
long_cities = [city for country in country_list for city in country if len(city) >= 6]
print(long_cities)
# long_cities = []
for country in country_list:
    for city in country:
        if len(city) >= 6:
            long_cities.append(city)

print(long_cities)
