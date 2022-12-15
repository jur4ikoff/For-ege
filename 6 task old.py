def abc(s):
    s = (s + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    return int(n)


for i in range(6, 10000):
    if abc(i) == 66:
        print(i)
        break
