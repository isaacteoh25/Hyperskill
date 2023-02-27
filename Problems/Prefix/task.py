def has_prefix(word, prefix):
    # return word.startswith(prefix)
    # for i in range(len(prefix)):
    #     if word[i] != prefix[i]:
    #         return False
    # return True
    for el1, el2 in zip(word, prefix):
        if el1 != el2:
            return False
    return True

prefix = input()
words = input().split()
# prefix ="proto"
# words ="We know so many words: proton and prototype and protoplasm and Protozoa.".split()

for word in words:
    if has_prefix(word, prefix):
        print(word)