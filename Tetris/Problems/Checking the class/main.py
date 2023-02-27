# print(countries.index("Bulgaria"))

# Is it a correct tuple? yes
# Can it be used as a dictionary key? no
# What is the result of the function len(hobbies)?
hobbies = ('reading', ['jogging', 'boxing', 'yoga'], 'movies', 'painting', ('photographing',))

print(len(hobbies))

dragons = ['Rudy', 'Targent', 'Aggie']
dragons.sort()
dragons = sorted(dragons, key=len)
dragons.reverse()

numbers = [1, 6, -9, 2.5, 4, 0]
numbers.sort(reverse=True)
sorted_numbers = sorted(numbers, reverse=True)


def nighttime(func):
    def wrapper(name):
        print('It is nighttime')
        return func(name)

    return wrapper


@nighttime
def get_message(name):
    print('We can hear some night birds like', name)


get_message('owls')