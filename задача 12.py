for i in range(99999999, 0, -1):
    x = i
    a, b = 1, 0

    while x > 0:
        d = x % 10
        a *= d
        if d > 5:
            b += d

        x //= 10

    if a == 8820:
        print(b)
        break