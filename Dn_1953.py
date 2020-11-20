from _collections import deque
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def runn(x, y, t):
    global visit
    q = deque()
    q.append((x, y, t))
    while len(q) > 0:
        x, y, t = q.popleft()
        if t == L-1:
            return
        if subway[x][y] == 0:
            pass
        elif subway[x][y] == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    if i == 0 and subway[nx][ny] in [1, 2, 5, 6]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 1 and subway[nx][ny] in [1, 2, 4, 7]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 2 and subway[nx][ny] in [1, 3, 4, 5]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 3 and subway[nx][ny] in [1, 3, 6, 7]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t+1))

        elif subway[x][y] == 2:
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    if i == 0 and subway[nx][ny] in [1, 2, 5, 6]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 1 and subway[nx][ny] in [1, 2, 4, 7]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))

        elif subway[x][y] == 3:
            for i in range(2, 4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    if i == 2 and subway[nx][ny] in [1, 3, 4, 5]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 3 and subway[nx][ny] in [1, 3, 6, 7]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))

        elif subway[x][y] == 4:
            for i in [0, 3]:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    if i == 0 and subway[nx][ny] in [1, 2, 5, 6]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 3 and subway[nx][ny] in [1, 3, 6, 7]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))

        elif subway[x][y] == 5:
            for i in [1, 3]:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    if i == 1 and subway[nx][ny] in [1, 2, 4, 7]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 3 and subway[nx][ny] in [1, 3, 6, 7]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))

        elif subway[x][y] == 6:
            for i in [1, 2]:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    if i == 1 and subway[nx][ny] in [1, 2, 4, 7]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 2 and subway[nx][ny] in [1, 3, 4, 5]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))

        elif subway[x][y] == 7:
            for i in [0, 2]:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    if i == 0 and subway[nx][ny] in [1, 2, 5, 6]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
                    elif i == 2 and subway[nx][ny] in [1, 3, 4, 5]:
                        visit[nx][ny] = 1
                        q.append((nx, ny, t + 1))
        # print(t)

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    subway = []
    for _ in range(N):
        subway.append(list(map(int, input().split())))
    # print(subway)
    visit = list([0] * M for _ in range(N))
    visit[R][C] = 1
    runn(R, C, 0)
    # print(visit)
    cnt = 0
    for i in range(len(visit)):
        for j in range(len(visit[i])):
            if visit[i][j] == 1:
                cnt += 1
    print(f'#{tc} {cnt}')