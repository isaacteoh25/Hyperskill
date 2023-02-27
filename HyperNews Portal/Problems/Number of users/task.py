# write your code here
import json

with open("users.json", "r") as json_file:
    user_dict_from_json = json.load(json_file)
total = 0
count = sum(len(v) for v in user_dict_from_json.values())
# for value in user_dict_from_json:
#     value_list = dict[value]
#     count = len(value_list)
#     total += count
cnt = 0
for usr in user_dict_from_json.items():
    for name in usr[1]:
        cnt += 1
print(cnt)
print(sum(map(len, user_dict_from_json.values())))
print(len(user_dict_from_json['users']))
print(count)  # True
print(len(user_dict_from_json.get('users')))