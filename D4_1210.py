T = 10
for t in range(1, T+1):
    testcase = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    a = ladder[99].index(2)
    b = 99
    dontgo = 0
    while b >= 0:
        if (dontgo == 0 or dontgo == 1) and a > 0 and ladder[b][a-1] == 1:
            a -= 1
            dontgo = 1
        elif (dontgo == 0 or dontgo == 2) and a < 99 and ladder[b][a+1] == 1:
            a += 1
            dontgo = 2
        else:
            b -= 1
            dontgo = 0
    print(f'#{t} {a}')




