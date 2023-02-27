def price_string(func):
    def wrapper(arg):
        # return '£' + str(func(arg))
        print( '£' + str(func(arg)))

    return wrapper  

@price_string
def new_price(arg):
    n_price = 90/100 * arg
    # print(n_price)
    return n_price

new_price(100)