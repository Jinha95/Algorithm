dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def mountain(x, y, k, cnt):
    global result
    if result < cnt+1:
        result = cnt+1
    visit[x][y] = 1
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if (0 <= nx < N) and (0 <= ny < N) and (visit[nx][ny] == 0):
            if board[nx][ny] < board[x][y]:
                mountain(nx, ny, k, cnt+1)
            elif board[nx][ny] - k < board[x][y]:
                a = board[nx][ny]
                board[nx][ny] = board[x][y] - 1
                mountain(nx, ny, 0, cnt+1)
                board[nx][ny] = a
    visit[x][y] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(board)
    # 가장 높은 봉우리 찾기
    maxheight = max(map(max, board))
    # print(maxheight)
    # 높은 봉우리를 가진 좌표값 모두 저장
    maxh = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == maxheight:
                maxh.append((i, j))
    # print(maxh)
    result = 0
    for i in maxh:
        visit = list([0]*N for _ in range(N))
        mountain(i[0], i[1], K, 0)
    print(f'#{tc} {result}')
