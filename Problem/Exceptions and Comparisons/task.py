def check_w_letter(word):
    if "w" in word:
        raise WordError
    return word
class WordError(Exception):
    pass