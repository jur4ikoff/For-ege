with open(file="24var04.txt", mode='r') as f:
    s = f.read()
    s = s.replace('AB', '5')

    min_cnt, cur_a_cnt, cur_cnt = 1000, 0, 0

    for i in range(len(s)):
        if s[i] == '5':
            c = i
            f = True
            while cur_a_cnt <= 21:
                try:
                    if s[c] == '5':
                        cur_a_cnt += 1
                    cur_cnt += 1
                except:
                    f = False
                    break
                c += 1

            if f:
                min_cnt = min(min_cnt, cur_cnt)

        cur_cnt = 0
        cur_a_cnt = 0

    print(min_cnt)