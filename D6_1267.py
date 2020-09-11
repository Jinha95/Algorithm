def bfs(startnum):
    if visit[startnum] == 1:
        pass
    else:
        q = [startnum]
        visit[startnum] = 1
        result = []
        while len(q) > 0:
            for _ in range(len(q)):
                a = q.pop(0)
                result += [a]
                for i in graph[a]:
                    b = 0
                    if visit[i] == 0:
                        for j in range(1, V+1):
                            if visit[j] == 0:
                                if j != a:
                                    if i in graph[j]:
                                        b += 1
                        if b == 0:
                            visit[i] = 1
                            q.append(i)
        return result

T = 10
for t in range(1, T+1):
    V, E = map(int, input().split()) # 그래프 정점의 총 수, 간선의 총 수
    li = list(map(int, input().split()))
    info = []
    for i in range(0, 2*E, 2):
        info.append(li[i:i+2])
    graph = [[] for _ in range(V+1)]
    visit = [0]*(V+1)
    for i in info:
        graph[i[0]] += [i[1]]
    # print(graph)
    f = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            f += [graph[i][j]]
    # print(f)
    start = []
    for i in range(1, V+1):
        if i not in f:
            start += [i]
    # print(start)
    reresult = []
    for i in range(len(start)):
        startnum = start[i]
        reresult += bfs(startnum)
    print(f'#{t}', end = " ")
    for i in reresult:
        print(i, end=" ")
    print()