s = input()
S = s.upper()
li = [0]* 26
if len(S) == 1:
    print(S)
else:
    for i in S:
        li[ord(i)-65] = li[ord(i)-65] + 1
    a = max(li)

    cnt = 0

    for i in li:
        if i == a:
            cnt += 1
    if cnt >= 2:
        print('?')
    else:
        b = li.index(a)
        print(chr(b+65))

