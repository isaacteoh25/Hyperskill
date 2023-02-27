import numpy as np

def custom_sum(arg1, arg2):
    a, b = isinstance(arg1, list), isinstance(arg2, (list))
    c, d = isinstance(arg1, np.ndarray), isinstance(arg2, (np.ndarray))
    if a and b:
        return 'Both arguments are lists, not arrays'
    elif c and d:
        return arg1 + arg2
    else:
        return 'One argument is a list'