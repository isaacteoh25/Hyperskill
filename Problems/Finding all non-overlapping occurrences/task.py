import re
def find_no_overlaps(text, pattern):
    return [m.start() for m in re.finditer(pattern, text)]

a = find_no_overlaps(input(), input())
# a = find_no_overlaps("aaaaa", "aa")

if not a:
   print(-1)
else:
    for i in a:
      print(i, end= ' ')


def find_no_overlaps(text, pattern):
    _pos = 0
    index_pos = []
    while True:
        _pos = text.find(pattern, _pos)
        if _pos > -1:
            index_pos.append(_pos)
            _pos = _pos + len(pattern)
        else:
            break
    if len(index_pos) == 0:
        return [-1]
    return index_pos

my_text = input()
my_pattern = input()
print(*find_no_overlaps(my_text, my_pattern))


def find_no_overlaps(text, pattern):
    list_ = []
    i = 0
    while i <= len(text) - len(pattern):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                i += 1
                found = False
                break

        if found:
            list_.append(i)
            i += len(pattern)

    return list_ if list_ else [-1]


print(*find_no_overlaps(input(), input()))