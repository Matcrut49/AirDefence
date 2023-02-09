from itertools import product
a = [1, 3]
c = [2, 4]
for i, b in product(a, c):
    print(i, b)