from itertools import product

print('x y z')

for x, y, z in product([0, 1], repeat=3):
    f = (x == z) or (x <= (y and z))
    if f == 0:
        print(x, y, z)
