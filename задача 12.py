s = '7' * 2022

while '777' in s or '333' in s:
    s = s.replace('777', '3', 1)
    s = s.replace('333', '7', 1)


print(s)