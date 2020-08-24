T = int(input())
for t in range(1, T+1):
    li = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0
    for i in range(9):
        a = list(set(li[i]))
        if len(a) == 9:
            cnt += 1

    li_li = []
    for i in range(9):
        for j in range(9):
            li_li += [li[j][i]]
        a = list(set(li_li))
        if len(a) == 9:
            cnt += 1
        li_li = []

    li_li_li = []
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            for z in range(x, x+3):
                for k in range(y, y+3):
                    li_li_li += [li[z][k]]
            a = list(set(li_li_li))
            if len(a) == 9:
                cnt += 1
            li_li_li = []

    if cnt == 27:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
