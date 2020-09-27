def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = [[start_x, start_y]]
    result = 0
    x = q[0][0]
    y = q[0][1]
    visited[x][y] = 1
    while len(q) > 0:
        for _ in range(len(q)):
            a = q.pop(0)
            if miro[a[0]][a[1]] == 3:
                return result
            for i in range(4):
                nx = a[0] + dx[i]
                ny = a[1] + dy[i]
                if 0 <= nx < N and 0 <= ny < N and miro[nx][ny] != 1:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
        result += 1
    return 1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    # print(miro)
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_x = i
                start_y = j
            if miro[i][j] == 3:
                end_x = i
                end_y = j
    visited = [[0] * N for _ in range(N)]
    # print(visited)
    sol = bfs(start_x, start_y)-1
    print(f'#{t} {sol}')
