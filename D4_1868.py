from collections import deque

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def BFS(r, c):
    #큐에 초기값 넣고 방문 표시
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        curr_r, curr_c = q.popleft() #하나 꺼내기
        for i in range(8):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if 0 <= nr < N and 0<= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                if game[nr][nc] == 0: #연쇄적으로 0이 나온다면 자동으로.
                    q.append((nr, nc))

# 8방향 탐색으로 주변에 몇개의 지뢰가 있는지
def mine_check(r, c):
    cnt = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        # continue는 밑에를 실행하지 않고 다음 i로 넘어간다.
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if game[nr][nc] == '*': cnt += 1
    return cnt

for tc in range(1, int(input())+1):
    N = int(input())
    game = [list(input()) for _ in range(N)]

    # 내 주변의 지뢰의 수로 2차원 리스트를 갱신
    zero_list = []
    for i in range(N):
        for j in range(N):
            if game[i][j] == '.':
                # 지뢰의 수로 2차원 리스트를 갱신함
                game[i][j] = mine_check(i, j)
            if game[i][j] == 0:
                zero_list.append((i, j))

    ans = 0 # 클릭횟수
    # 주변에 지뢰가 하나도 없는 값들을 먼저 클릭
    visited = [[False] * N for _ in range(N)]
    for r, c in zero_list:
        # 이미 방문했다면 다음 r, c 로 넘어가고
        if visited[r][c]: continue
        # 방문하지 않았다면
        BFS(r, c)
        ans += 1

    # 나머지 지뢰가 아닌 값들을 클릭 -> 어차피 한칸씩 밖에 클릭이 안됨
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and game[i][j] != '*':
                ans += 1
    print(f'#{tc} {ans}')