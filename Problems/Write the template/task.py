import re

import numpy as np

string_1 = 'I love Python 3'
string_2 = 'i love Pitsaw'
string_3 = 'we love Papuan'
string_4 = 'we love php'
template = '[a-zA-Z ]{2,3}love P.*'
# template = '..? love P'
# template = '.?.? love P.?.?.?.?.?..?'
# template = '(.*)(love P)(.*)'
# print(re.match(template, string_1))
# print(re.match(template, string_2))
# print(re.match(template, string_3))
# print(re.match(template, string_4))
# string = 'Backslash is your best friend, right?'
# string = re.escape(string)
# print(string)
# good_string = '03.12.2008'
# bad_string = '03-12-2008'
# template = '03\.'
# print(re.match(template, good_string))
# print(re.match(template, bad_string))
# 2000 to 2019
# print(re.match('^([2][0][01][0-9])$', '2020') )
# ^[a-zA-Z 0-9\.\,\+\-]*$
print(re.match('[a-zA-Z0-9]{1,2}', '12'))
print(re.match('^([0][01][0-9])$', '2020') )
print(re.match(':[)\-(o]{1,2}', ':-o') )
regex = r'python[^\s^\W]*$'
# regex = r'python\B'
print(re.match(regex,'python,'))
print(re.match('ab+a','aa'))
print(re.match('\d.*?\d','123abc456'))

a = np.array([9, 99, 999])
array = np.array([[1,  2,  3],
                  [4,  5,  6],
                  [7,  8,  9],
                  [10, 11, 12]])
print(array)