def bfs(start):
    q = [start]
    visit[start] = 1
    while len(q) > 0:
        for _ in range(len(q)):
            a = q.pop(0)
            for i in info[a]:
                if visit[i] == 0:
                    visit[i] = 1
                    q.append(i)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # 마을의 사람 수, 서로를 아는 사람의 관계 수
    visit = [0] * (N + 1)
    info = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        info[x].append(y)
        info[y].append(x)
    result = 0
    for k in range(1, N+1):
        if visit[k] == 0:
            start = k
            bfs(start)
            result += 1

    print(f'#{t} {result}')