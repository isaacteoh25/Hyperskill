import copy


def print_book_info(title, author=None, year=None):
    #  Write your code here
    if author is None and year is None:
        print('"{0}"'.format(title))
    elif author is None:
         print('"{0}" was written in {1}'.format(title,  year))
    elif year is None:
         print('"{0}" was written by {1}'.format(title, author))
    else:
        print('"{0}" was written by {1} in {2}'.format(title, author, year))

    def print_book_info(title, author=None, year=None):
        if author and year:
            print(f'"{title}" was written by {author} in {year}')
        else:
            print(
                f'"{title}"{(author or "") and " was written by " + author} {(year or "") and "was written in " + year}')

a = [1, 2, 3]
b = a
# what is the value of b?
print(b)
a[1] = 10
# and here?
print(b)
b[0] = 20
# what about now?
print(b)
a = [5, 6]
print(b)
lst = [2, 4, 8]


def blackbox(lst):
    lst[0]= 1
    return lst


my_list = [2, 4, 6]
new_list = blackbox(my_list)
print(new_list)
print('modifies' if my_list is new_list else 'new')

lissst = [2, 4, 6]
# my_copy = [lissst[0], lissst[1], lissst[2]]
my_copy = copy.deepcopy(lissst)
# my_copy = copy.copy(lissst)
# mycopy = lissst.copy()
# print(my_copy[0])
print(id(my_copy), id(lissst)) # 140294825858224 140294826282752 - id of new list differ
print(id(my_copy[0]))  # 4394239104 4394239104 - ids of its elements is the same
def solve(obj):
    if copy.deepcopy(obj) is copy.copy(obj):
        return False
    return True


lst = [[5, 5], [2, 3, 9]]
new_lst = copy.deepcopy(lst)
new_lstc = copy.copy(lst)
new_copy_lst = lst.copy()
lst[0].append(5)

print(lst)                     # [[5, 5, 5], [2, 3, 9]]
print(new_lst)                 # [[5, 5], [2, 3, 9]]
print(new_lstc)
print(new_copy_lst)


def copying_machine(obj):
    # if copy_mode == "deep copy":
    #     my_copy = copy.deepcopy(obj)
    # else:
        my_copy = obj.copy()
        return my_copy


def detect_copy():
    list1 = [1, 2, 3]
    list2 = [list1]
    list3 = copying_machine(list2)
    return f'{"shallow" if list3[0] is list1 else "deep"} copy'