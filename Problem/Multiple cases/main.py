def f1(x):
    y = (x ** 2) + 1
    return y


def f2(x):
    y = 1 / (x ** 2)
    return y


def f3(x):
    y = (x * x) - 1
    return y


# def f(x):
#     x = float(x)
#     if x <= 0:
#         print(f1(x))
#
#     elif 0 < x < 1:
#         print(f2(x))
#
#     else:
#         print(f3(x))
def f(x):
    x = float(x)
    if x <= 0:
        return f1(x)
    if 0 < x < 1:
        return f2(x)
    return f3(x)
# print(f(1))
# print(f(0.1))
# print(f(100))