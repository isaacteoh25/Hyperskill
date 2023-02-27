# # write your code here
import re
i = input().split('|')

print(bool(re.search(i[0].replace("'", ""),i[1].replace("'", ""))))
# # print(bool(re.match(b[0],b[1])))
#stage 3
# import sys
# sys.setrecursionlimit(10000)
#
# regex, word = input().split("|")
#
#
# def compare(reg, char):
#     return reg == "." or reg == char or not reg
#

# def compare_recursion(reg, char):
#     if len(reg) == 0:
#         return True
#     if len(char) == 0:
#         return False
#     if compare(reg[0], char[0]):
#         return compare_recursion(reg[1:], char[1:])
#     else:
#         return False
#
#
# def new_compare(reg, char):
#     if compare_recursion(reg, char):
#         return True
#     elif not char:
#         return False
#     else:
#         return new_compare(reg, char[1:])
#
# print(new_compare(regex, word))


def match(regexp, str_, check=0):
    if not regexp:
        if check == 2 and str_:
            return False
        return True
    elif not str_:
        return False
    elif regexp[0] == '^' and regexp[-1] == '$':
        return match(regexp[1:-1], str_, check=2)
    elif regexp[0] == '^':
        return match(regexp[1:], str_, check=1)
    elif regexp[-1] == '$':
        return match(regexp[:-1], str_[-len(regexp):], check)
    elif regexp[0] == '\\' and regexp[1] == str_[0]:
        return match(regexp[2:], str_[1:], check)
    elif regexp[0] == '\\' and regexp[1] != str_[0] and check == 1:
        return False
    elif len(regexp) > 1:
        if regexp[1] in ('?', '*') and str_[0] != regexp[0]:
            return match(regexp[2:], str_, check)
        elif regexp[1] == '?' and regexp[0] in (str_[0], '.'):
            return match(regexp[2:], str_[1:], check=1)
        elif regexp[1] in ('*', '+') and regexp[0] in (str_[0], '.'):
            point = str_[0]
            while point == str_[0]:
                str_ = str_[1:]
                if not str_:
                    return True
            return match(regexp[2:], str_, check)
    if regexp[0] in (str_[0], '.'):
        check =(1 if not check else check)
        return match(regexp[1:], str_[1:], check)
    elif not check:
        return match(regexp, str_[1:], check)
    else:
        return False


if __name__ == '__main__':
    print(match(*input().split('|')))