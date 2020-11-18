def dijstra():
    dist = [987654321] * (V+1)
    visit = [False] * (V+1)
    dist[0] = 0
    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):
            if not visit[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visit[min_idx] = True

        for j in range(V+1):
            if not visit[j] and dist[j] > dist[min_idx]+adj[min_idx][j]:
                dist[j] = dist[min_idx] + adj[min_idx][j]

    return dist[V]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[987654321] * (V+1) for _ in range(V+1)]

    for i in range(E):
        st, ed, w = map(int, input().split())

        adj[st][ed] = w

    print(f'#{tc} {dijstra()}')