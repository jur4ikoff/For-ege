def task(n):
    r = bin(n)[2:]
    r = r[1:]
    r = int(r, base=2)
    return n - r

a = []
for i in range(100, 3001):
    a.append(task(i))

print(len(set(a)))