def bfs(start, end):
    if start == end:
        return 0
    result = 0
    q = [start]
    visited[start] = 1
    while len(q) > 0:
        result += 1
        for _ in range(len(q)):
            a = q.pop(0)
            for i in info[a]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
        if end in q:
            return result
    return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    info = [[] for _ in range(V+1)]     # [ [], [], [], [], [], [], [] ]
    visited = [0] * (V+1)   # [0, 0, 0, 0, 0, 0, 0]
    # 간선 정보. info의 index는 출발 노드를 뜻함. value는 도착 노드
    for i in range(E):
        x, y = map(int, input().split())
        info[x].append(y)
        info[y].append(x)

    start, end = map(int, input().split())
    sol = bfs(start, end)
    print(f'#{t} {sol}')
