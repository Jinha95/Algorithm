from _collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def gogo(x, y):
    q = deque()
    q.append((x, y))
    while len(q) > 0:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dis[nx][ny] > dis[x][y] + board[x][y]:
                    dis[nx][ny] = dis[x][y] + board[x][y]
                    q.append((nx, ny))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input())))
    # print(board)
    inf = 987654321
    dis = list([inf] * N for _ in range(N))
    dis[0][0] = 0
    # print(dis)
    gogo(0, 0)
    print(f'#{tc} {dis[N-1][N-1]}')