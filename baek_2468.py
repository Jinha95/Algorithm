import sys
sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def rain(x, y, h):
    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == False and board[nx][ny] > h:
            visit[nx][ny] = True
            rain(nx, ny, h)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
maxrain = max(map(max, board))
minrain = min(map(min, board))

result = 0

for i in range(0, maxrain):
    cnt = 0
    visit = list([False]*N for _ in range(N))
    for q in range(N):
        for w in range(N):
            if board[q][w] > i and visit[q][w] == False:
                visit[q][w] = True
                rain(q, w, i)
                cnt += 1
    result = max(cnt, result)

print(result)
