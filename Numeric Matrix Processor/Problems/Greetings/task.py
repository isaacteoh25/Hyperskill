def morning(func):
    def wrapper(name):
        func(name)
        print('Good morning,', name)

    return wrapper

# @morning
# def greetings(name):
#     print('Hello,', name)
#
# greetings('Susie')