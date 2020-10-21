def sunpyo(x, y):
    if visit[x] == 0:
        visit[x] = 1
        if mag[x-1][2] != mag[x][6] and mag[x-1][2] != 2:
            if mag[x + 1][6] != mag[x][2] and mag[x+1][6] != 2:
                if y == 1:
                    mag[x] = [mag[x][7]] + mag[x]
                    del mag[x][8]
                    if visit[x-1] == 0 and 0 < x-1 < 5:
                        sunpyo(x-1, -1)
                    if visit[x+1] == 0 and 0 < x+1 < 5:
                        sunpyo(x+1, -1)
                else:
                    mag[x].append(mag[x][0])
                    del mag[x][0]
                    if visit[x-1] == 0 and 0 < x - 1 < 5:
                        sunpyo(x - 1, 1)
                    if visit[x+1] == 0 and 0 < x + 1 < 5:
                        sunpyo(x + 1, 1)
            else:
                if y == 1:
                    mag[x] = [mag[x][7]] + mag[x]
                    del mag[x][8]
                    if visit[x-1] == 0 and 0 < x - 1 < 5:
                        sunpyo(x-1, -1)
                else:
                    mag[x].append(mag[x][0])
                    del mag[x][0]
                    if visit[x-1] == 0 and 0 < x - 1 < 5:
                        sunpyo(x-1, 1)
        elif mag[x + 1][6] != mag[x][2] and mag[x+1][6] != 2:
            if y == 1:
                mag[x] = [mag[x][7]] + mag[x]
                del mag[x][8]
                if visit[x+1] == 0 and 0 < x + 1 < 5:
                    sunpyo(x + 1, -1)
            else:
                mag[x].append(mag[x][0])
                del mag[x][0]
                if visit[x+1] == 0 and 0 < x + 1 < 5:
                    sunpyo(x + 1, 1)
        else:
            if y == 1:
                mag[x] = [mag[x][7]] + mag[x]
                del mag[x][8]
            else:
                mag[x].append(mag[x][0])
                del mag[x][0]

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    mag = [[2]*8] + mag + [[2]*8]
    info = [list(map(int, input().split())) for _ in range(K)]
    visit = [0, 0, 0, 0, 0, 0]
    for i in info:
        a = i[0]
        b = i[1]
        sunpyo(a, b)
        visit = [0, 0, 0, 0, 0, 0]
    result = mag[1][0] + (2 * mag[2][0]) + (4 * mag[3][0]) + (8 * mag[4][0])
    # print(mag[1])
    # print(mag[2])
    # print(mag[3])
    # print(mag[4])
    print(f'#{tc} {result}')
