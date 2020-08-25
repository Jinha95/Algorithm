T = int(input())
for t in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for n in range(N)]
    case = [['.' for _ in range(10)] for _ in range(10)]

    for i in li:
        for j in range(i[0], i[2]+1):
            for k in range(i[1], i[3]+1):
                if i[4] == 1:
                    case[j][k] += 'a'
                else:
                    case[j][k] += 'b'


    cnt = 0
    for x in range(10):
         for y in range(10):
             if 'a' in case[x][y] and 'b' in case[x][y]:
                cnt += 1
    print(f'#{t} {cnt}')
