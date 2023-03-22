def fibonacci(n):
    if n > 1:
        x, y = 0, 1
        while (n > 0):
            yield x
            # x, y = y, x + y
            y = x + y
            x = y - x
            # x, y = y, x + y
            n -= 1
        # print()


# fibonacci(5)
# multiples_of_three =fibonacci(5)
# print(next(multiples_of_three))