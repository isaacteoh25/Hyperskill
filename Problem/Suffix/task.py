def has_suffix(word, suffix):
    # return word.endswith(suffix)
    # for letter1, letter2 in zip(word[::-1], suffix[::-1]):
    #     if letter1 != letter2:
    #         return False
    # return True
    # for i in range(len(word) - len(suffix) + 1):
    #     found = True
    #
    #     for j, _k in enumerate(suffix):
    #         if word[i + j] != suffix[j]:
    #             found = False
    #             break
    #
    #     if found:
    #         return True
    #
    # return False
    if len(word) <= len(suffix):
        return False
    return word[-len(suffix):] == suffix
# Change the next line
extension = ".py"
n = int(input())

for i in range(n):
    file = input()
    if has_suffix(file, extension):
        print(file)