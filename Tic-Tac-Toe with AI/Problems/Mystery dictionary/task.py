# `random_dict` has been defined
# the input is in the variable `word`
# write the rest of the code here
from collections import defaultdict
 
# freq_defaultdict = defaultdict(string)
# Dictionary1 = { 'A': 'Geeks', 'B': 'For'} 
  
# using setdefault() method 
# when key is not in the Dictionary 
# a = string(input())
Third_value = random_dict.setdefault(word) 
if Third_value == None:
    print("Not in the dictionary")
else:
    print(Third_value)

# print(random_dict.setdefault(word, "Not in the dictionary"))