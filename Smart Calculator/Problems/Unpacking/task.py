def unpack(input_tuple):
    result = []
    for item in input_tuple:
        if isinstance(item, tuple):
            result.extend(unpack(item))
        else:
            result.append(item)
    unpacked = tuple(result)
    return unpacked
