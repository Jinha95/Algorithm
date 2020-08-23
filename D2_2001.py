T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for n in range(N)]
    start = 0
    result = []
    for r in range(N):
        for c in range(N):
            cnt = 0
            if r + M - 1 < N and c + M - 1 < N:
                cnt = 0
                for i in range(r, r+M):
                    for j in range(c, c+M):
                        cnt += li[i][j]
                result.append(cnt)
    maxresult = max(result)
    print(f'#{t} {maxresult}')