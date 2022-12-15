def find_del(n):
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i  # наибольший делитель

    return -1  # простое число


count = 0
for i in range(550001, 1000000000):
    if find_del(find_del(i)) != -1:
        print(i, count)
        count += 1
    if count > 6:
        break

