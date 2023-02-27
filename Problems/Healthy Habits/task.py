# the list "walks" is already defined
# your code here
walks = [
    {"day": "Monday", "distance": 2000},
    {"day": "Tuesday", "distance": 3000},
    {"day": "Wednesday", "distance": 3500},
    {"day": "Thursday", "distance": 2500},
    {"day": "Friday", "distance": 2500},
    {"day": "Saturday", "distance": 1000},
    {"day": "Sunday", "distance": 5600}]
print(round(sum(item['distance'] for item in walks)/len(walks)))
print(sum(map(lambda x: x['distance'], walks)) // len(walks))
distance = 0
for a_dict in walks:
    distance += a_dict.get('distance')
print(distance // len(walks))