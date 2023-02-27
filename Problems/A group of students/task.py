from typing import NamedTuple
from operator import attrgetter


def multi_sort(data, specs):

    for key, reverse in reversed(specs):
        data.sort(key=attrgetter(key), reverse=reverse)
    return data


class Student(NamedTuple):
    name: str
    age: int


students = []
num = int(input())
for i in range(num):
    name, age =input().split()
    students.append(Student(name, age))
multi_sort(students, (('age', False), ('name', False)))
for student in students:
    print(student[0])


def partition(lst, start, end):
    three = [(lst[start], start),
             (lst[(start + end) // 2], (start + end) // 2),
             (lst[end], end)]
    three.sort()
    lst[start], lst[three[1][1]] = lst[three[1][1]], lst[start]
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


def quick_sort(lst, start, end):
    if start >= end:
        return

    j = partition(lst, start, end)
    quick_sort(lst, start, j - 1)
    quick_sort(lst, j + 1, end)


n = int(input())
students = []
for _ in range(n):
    students.append(list(input().split()))
students = list(map(lambda x: [int(x[1]), x[0]], students))
quick_sort(students, 0, len(students) - 1)
for elem in students:
    print(elem[1])