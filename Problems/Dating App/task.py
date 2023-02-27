
names = []
def select_dates(potential_dates):
    for i in potential_dates:
        if i["age"] > 30 and "art" in i["hobbies"] and "Berlin" in i["city"]:
            names.append(i["name"])
    return ", ".join(names)

def select_dates(potential_dates):
    return ', '.join([match['name'] for match in potential_dates if
                      match['age'] > 30 and 'art' in match['hobbies'] and match['city'] == 'Berlin'])

    # print(", ".join(names))

# potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
#                         "hobbies": ["jogging", "music"], "city": "Hamburg"},
#                        {"name": "Sasha", "gender": "male", "age": 18,
#                         "hobbies": ["rock music", "art"], "city": "Berlin"},
#                        {"name": "Maria", "gender": "female", "age": 35,
#                         "hobbies": ["art"], "city": "Berlin"},
#                        {"name": "Daniel", "gender": "non-conforming", "age": 50,
#                         "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
#                        {"name": "John", "gender": "male", "age": 41,
#                         "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]
# select_dates(potential_dates)