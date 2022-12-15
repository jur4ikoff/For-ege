for i in range(1, 1000000): # а
    is_ok = True
    for j in range(1, 30000): # Значение X
        is_ok *= (j % 45 == 0 or j % 15 != 0 or j % i == 0)
    if is_ok:
        print(i)
        break
