def task(n):
    r = bin(n)[2::]
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '1'
    else:
        r = '11' + r[2:] + '0'

print(task)