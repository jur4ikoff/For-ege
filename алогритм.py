for i in range(0, 10000):
    bin_i = bin(i)[2:]
    if i % 2 == 0:
        bin_i += '10'
    else:
        bin_i += '11'
    bin_i += '0' if bin_i.count('1') % 2 == 0 else '1'

    if int(str(bin_i), 2) > 53:
        print(int(str(bin_i), 2))
        print(i)
        break