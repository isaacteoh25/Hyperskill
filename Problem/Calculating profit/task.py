weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]
revenues = [10,20, 30]
costs = [1,2, 3]
# for a, b, c in zip(months, revenues, costs):
#     print(a, b - c)

for i in zip(weekdays, revenues, costs):
    print(i[0], i[1] - i[2])
