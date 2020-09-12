def dfs(x, y, v):
    global result
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and room[nx][ny] == v+1:
            result += 1
            s = room[nx][ny]
            dfs(nx, ny, s)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    reresult = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result = 1
            dfs(i, j, room[i][j])
            reresult[i][j] += result
    # print(reresult)
    a = max(map(max, reresult))
    # print(a)
    rerere = []
    for i in range(N):
        for j in range(N):
            if reresult[i][j] == a:
                rerere += [room[i][j]]
    b = min(rerere)
    print(f'#{t} {b} {a}')
