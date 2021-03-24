from functools import reduce
from itertools import groupby

# ========= Mapping ==========
words = ['Deer', 'Bear', 'River', 'Car',
         'Car', 'River', 'Deer', 'Car', 'Bear']
mapping = map((lambda x: (x, 1)), words)
print(mapping)
# output:
# [('Deer', 1), ('Bear', 1), ('River', 1), ('Car', 1),
# ('Car', 1), ('River', 1), ('Deer', 1), ('Car', 1), ('Bear', 1)]

# ========= Shuffling ==========
sorted_mapping = sorted(mapping)
print(sorted_mapping)
# output:
# [('Bear', 1), ('Bear', 1), ('Car', 1), ('Car', 1),
# ('Car', 1), ('Deer', 1), ('Deer', 1), ('River', 1), ('River', 1)]

# ========= Reducing ==========
grouper = groupby(sorted_mapping, lambda p: p[0])
final = map(lambda l: (l[0], reduce(lambda x, y: x +
                                    y, map(lambda p: p[1], l[1]))), grouper)
print(list(final))
# output:
# [('Bear', 2), ('Car', 3), ('Deer', 2), ('River', 2)]
