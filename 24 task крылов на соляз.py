with open(r"D:\Downloads\informatika20.zip_pass_123\24var02.txt", 'r') as f:
    s = f.read()

    min_cnt, cur_a_cnt, cur_cnt = 1000, 0, 0

    for s1 in range(len(s)):
        if s[s1] == 'A':
            c = s1
            f = True
            while cur_a_cnt < 35:
                try:
                    if s[c] == 'A':
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