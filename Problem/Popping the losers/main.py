# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
# firms = OrderedDict(json.loads(input()))
# firms = {"YourHouse": 9.5, "BrownBuildCo": 9.1, "Build in the City": 9.0, "mr.Stone & Co": 7.8, "Flinstones Appartment": 7.3}
# your code here
# firms.popitem()
# firms.popitem()
# print(firms)

from collections import ChainMap


string_instruments = {'violin': 5, 'guitar': 7, 'viola': 2, 'banjo': 1}
percussion_instruments = {'castanets': 4, 'drum': 2, 'tambourine': 3, 'musical triangle': 1}

band = ChainMap(string_instruments, percussion_instruments)
print(band)
print(band.parents)

print(band.maps[1])
number = 12241
print(((number % 100) / 10) % 10)
