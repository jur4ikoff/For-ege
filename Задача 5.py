file = open("D:\\Изображения\\22.txt")
s = file.read()
file.close()

in_group = False
count = 0
c_count = 0
g_count = 0

for c in s:
    if c == 'D':
        if in_group:
            in_group = False

            if count >= 10 and c_count >= 2:
                g_count += 1
        else:
            in_group = True
            count = 1

    if in_group:
        count += 1

        if c == 'C':
            c_count += 1

print(g_count)