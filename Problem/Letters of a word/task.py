def letters(word):
    for w in word:
        yield w

    # yield from word

    # i = 0
    # while i < len(word):
    #     yield word[i]
    #     i += 1

# multiples_of_three =letters('python')
# print(next(multiples_of_three))
#
# numbers = [1, 2, 3]
#
# my_generator = (n ** 2 for n in numbers)
#

    # print(next(my_generator))
# letters('python')

# def multiples(a, n):
#     i = 1
#     while i <= n:
#         yield a*i
#         i += 1

# multiples_of_three = multiples(3, 5)
#
# # It produces the first 5 multiples of 3 one by one:
# print(next(multiples_of_three))