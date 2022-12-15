def a(x):
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        if x % 8 > 4:
            L = L + (x % 8)
        x = x // 8
    return L, M

for i in range(0, 100000):
    b, c = a(i)
    if b == 12 and c == 4:
        print(i)
        break
