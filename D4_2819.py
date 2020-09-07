def dfs(y, x, v):
    if len(v) == 7:
        sol.append(v)
        return sol
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            s = v + board[ny][nx]
            dfs(ny, nx, s)


T = int(input())
for t in range(1, T+1):
    board = [list(map(str, input().split())) for _ in range(4)]
    # print(board)
    sol = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j])
    sol = list(set(sol))

    print(f'#{t} {len(sol)}')

