def task(a, b):
    if a == 23 or a > b:
        return 0
    if a == b:
        return 1
    return task(a + 1, b) + task(a * 2, b)


print(task(3, 12) * task(12, 27))