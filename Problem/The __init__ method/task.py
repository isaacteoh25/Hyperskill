class NotWordError(Exception):
    def __init__(self, word):
        self.message = word + " is not a word, sorry!"
        super().__init__(self.message)

def check_word(word):
    if '0' in word:
        raise NotWordError(word)
    else:
        return word

def error_handling(word):
    try:
        a = check_word(word)
        print(a)
    except NotWordError as err:
        print(err)
# error_handling('al0')


# class LessThanFiveHundredError(Exception):
#     def __init__(self, num):
#         self.message = "The integer %s is below 500!" % str(num)
#         super().__init__(self.message)
#
#
# def example_exceptions_5(num):
#     if num < 500:
#         raise LessThanFiveHundredError(num)
#     else:
#         print(num)
# example_exceptions_5(50)