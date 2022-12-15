import sys
sys.setrecursionlimit(10000)

def task(a, b):
    if a < b or a == 4:
        return 0
    if a == b:
        return 1
    return task(a - 1, b) + task(a // 2, b)


print(task(60, 20) * task(20, 1))
