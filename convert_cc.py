def convert(num, to_base, from_base=10):
    tmp = int(str(num), from_base)
    new_num = ''
    while tmp > 0:
        new_num += str(tmp % to_base)
        tmp //= to_base

    return new_num[::-1]


print(convert(3, 2, 5))
