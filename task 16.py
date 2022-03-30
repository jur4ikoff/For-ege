def dolboeb(x):
    a, b = 1, 0
    while x > 0:
        d = x % 10
        a *= d
        if d > 5:
            b += d
        x //= 10
    return a, b

b_list = []
for i in range(0, 99999999):
    a, b = dolboeb(i)
    if a == 8820:
        b_list.append(b)

print(max(b_list))
