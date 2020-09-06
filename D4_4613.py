T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    info = [list(str(input())) for _ in range(N)]
    # print(info)
    line = []
    for i in range(1, N):
        for j in range(1, N):
            for k in range(1, N):
                if i+j+k == N:
                    line.append([i, j, k])
    # print(line) line이라는 리스트는 각 wbr이 차지하는 줄 수

    result = []

    for q in line:
        cnt = 0
        for w in range(q[0]):
            for z in range(M):
                if info[w][z] != 'W':
                    cnt += 1
        for e in range(q[0], q[0]+q[1]):
            for x in range(M):
                if info[e][x] != 'B':
                    cnt += 1
        for r in range(q[0]+q[1], q[0]+q[1]+q[2]):
            for c in range(M):
                if info[r][c] != 'R':
                    cnt += 1

        result.append(cnt)
    sol = min(result)
    print(f'#{t} {sol}')
