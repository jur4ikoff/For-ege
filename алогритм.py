def convert(num, to_base, from_base=10):
    tmp = int(str(num), from_base)
    new_num = ''
    while tmp > 0:
        new_num += str(tmp % to_base)
        tmp //= to_base

    return new_num[::-1]


for i in range(0, 100000):
    N = str(convert(i, 2))
    print(N)
    # if int(N) % 2 == 0:
    #     N += str('10')
    # else:
    #     N += str('11')
#
# tmp = N.replace('0', '')
# if len(tmp) % 2 == 0:
#     N += str('0')
# else:
#     N += str('1')
#
# output = convert(N, 10, from_base=2)
# if int(output) > 53:
#     print(i)
#     break
#
