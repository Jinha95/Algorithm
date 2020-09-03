def bfs(start):
    q = [start]
    visited[start] = 1
    result = 0
    resultlist = [[] for _ in range(101)]
    while len(q) > 0:
        result += 1
        for _ in range(len(q)):
            a = q.pop(0)
            for i in info[a]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    resultlist[result].append(i)

    sol = max(resultlist[result-1])
    return sol

T = 10
for t in range(1, T+1):
    N, start = map(int, input().split())
    li = list(map(int, input().split()))
    info = [[] for _ in range(101)]
    # 인덕스번호 : 출발점  value값 : 도착점
    for i in range(0, N, 2):
        info[li[i]].append(li[i+1])
    # print(info)
    visited = [0]*101
    sol = bfs(start)
    print(f'#{t} {sol}')