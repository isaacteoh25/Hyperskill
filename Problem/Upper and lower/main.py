# the list with words from string
# please, do not modify it
some_iterable = input().split()
# some_iterable = "Great loves too must be endured.".split()
# use dictionary comprehension to create a new dictionary
planets_diameter_mile = {a.upper(): a.lower() for a in
                         some_iterable}
print(planets_diameter_mile)

words = {}
for word in some_iterable:
    words[word.upper()] = word.lower()

print(words)