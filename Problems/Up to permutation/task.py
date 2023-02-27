# NO_OF_CHARS = 256
def contains_upto_permutations(str1, str2):
    # Create two count arrays and initialize 
    # all values as 0 
    # count1 = [0] * NO_OF_CHARS 
    # count2 = [0] * NO_OF_CHARS
    try:
        count1 = {}
        count2 = {}
        for i in str1:
            count1[i] = 0

        for i in str2:
            count2[i] = 0
        # For each character in input strings,
        # increment count in the corresponding
        # count array
        for i in str1:
            count1[i] =  str(int(count1[i]) + 1)

        for i in str2:
            count2[i] = str(int(count2[i]) + 1)

        # Compare count arrays
        for i in count2:
            if int(count2[i]) > int(count1[i]):
                return False
        return True
    except:
        return False

print(contains_upto_permutations(input(), input()))
# print(contains_upto_permutations("abracadabra","aacd"))

def contains_upto_permutations(text, pattern):
    pat_len = len(pattern)
    for i in range(len(text)):
        if sorted(text[i:pat_len + i]) == sorted(pattern):
            return True
    return False
tex = input()
pat = input()
print(contains_upto_permutations(tex, pat))

def contains_upto_permutations(text, pattern):
    for i in pattern:
        if text.count(i) < pattern.count(i):
            return False
    return True

print(contains_upto_permutations((input()), input()))

from collections import Counter

def contains_upto_permutations(text, pattern):
    for i in range(len(text) - len(pattern) + 2):
        if Counter(text[i:len(pattern) + i]) == Counter(pattern):
            return True
    return False

txt = input()
pat = input()
print(contains_upto_permutations(txt, pat))