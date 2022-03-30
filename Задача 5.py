def task(n):
    n = str(n)
    list_digit = []
    for i in range(len(n) + 1):
        try:
            s = n[i] + n[i + 1]
            list_digit.append(s)

        except IndexError:
            pass
    try:
        min_digit = min(list_digit)
        max_digit = max(list_digit)
        answer = int(min_digit) + int(max_digit)
        return answer
    except Exception:
        pass

for i in range(0, 1000000):
    if task(i) == 153:
        print(i)
        break


def task_6(s):
    s = s // 7
    n = 1
    while s < 255:
        s += n
        n += 1
    return n


count = 0
for i in range(0, 10000000):
    if task_6(i) == 8:
        count += 1

print(count)
