# import numpy as np
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# # a1 = np.array([[6, 7]])
# # a2 = np.array([[9, 0]])
# a1 = np.array([a, b])
# a2 = np.array([c, d])
# print(a1 < a2)
import re

template = 'and?'
# word =
r1 = re.findall(template,r'Humans are hardly the only interesting members of the animal kingdom. Research on the bodies and behaviors of our furry cousins can help scientists learn more about our own species’ evolution and cognition. And even when they don’t help unlock the ancient secrets of human ancestry, some animals are just too cute — or weird, or gross, or terrifying — not to get to know a little better.')
print(r1)