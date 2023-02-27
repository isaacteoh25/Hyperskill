def check_integer(num):
    if 45 < num < 67:
        return num
    else:
        raise NotInBoundsError
def error_handling(num):
    try:
        print(check_integer(num))
    except NotInBoundsError:
        print('There is an error!')

# i = int(input())
# check_integer(i)
