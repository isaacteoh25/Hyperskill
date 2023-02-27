# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
import json
from collections import OrderedDict

marks = OrderedDict(json.loads(input()))

# your code here
marks['Max'] = 100
# print(marks)
# my_ord_dict = OrderedDict(marks)
marks.move_to_end('Max', last=False)
print(marks)