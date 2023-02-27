transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

# create transaction_dict
from collections import defaultdict


# Turns transactions into a dictionary
transaction_dict = defaultdict(list)

# ----------------------------------------------------------
# Buils a dictionayy with values summed
for key, value in transactions:
    transaction_dict[key].append(value)

# for transaction in transactions:
#     transaction_dict[transaction[0]].append(transaction[1])

# for (j, k) in transactions:
#     transaction_dict.setdefault(j, []).append(k)

# for key, val in transactions:
#     transaction_dict.setdefault(key, []).append(val)

# for trans_id, spend in transactions:
#     transaction_dict.setdefault(trans_id, []).append(spend)

# def convert(tup, di):
#     for a, b in tup:
#         di.setdefault(a, []).append(b)
#     return di
# dictionary = {}
# transaction_dict = convert(transactions, dictionary)