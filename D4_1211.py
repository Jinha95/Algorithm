T = 10
for t in range(1, T+1):
    testcase = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    last_1 = list(filter(lambda x: ladder[99][x] == 1, range(len(ladder[99]))))
    dic = {}
    for i in range(len(last_1)):
        dontgo = 0
        cnt = 0
        b = 99

        while b >= 0:
            if (dontgo == 0 or dontgo == 1) and last_1[i] > 0 and ladder[b][last_1[i]-1] == 1:
                last_1[i] -= 1
                dontgo = 1
                cnt += 1
            elif (dontgo == 0 or dontgo == 2) and last_1[i] < 99 and ladder[b][last_1[i]+1] == 1:
                last_1[i] += 1
                dontgo = 2
                cnt += 1
            else:
                b -= 1
                dontgo = 0
                cnt += 1

        dic[last_1[i]] = cnt

    result = min(dic.keys(), key=lambda k : dic[k])

    print(f'#{t} {result}')




