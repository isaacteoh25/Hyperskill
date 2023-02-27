from collections.abc import Hashable


objects_dict = {key: hash(key) for key in objects if isinstance(key, Hashable)}

from collections.abc import Hashable

objects_dict = {}
for i in objects:
    if isinstance(i, Hashable):
        objects_dict[i] = i.__hash__()

hashable_list = [x for x in objects if isinstance(x, Hashable)]
list_of_hashes = [hash(x) for x in objects if isinstance(x, Hashable)]
objects_dict = dict(zip(hashable_list, list_of_hashes))