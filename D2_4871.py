# 잘 안되서 일단 Googling..

def dfs(start):
    visited[start] = 1
    stack.append(start)
    for i in range(1, V + 1):
        if matrix[start][i] == 1 and visited[i] != 1:
            visited[i] = 1
            dfs(i)
    return stack


T = int(input())
for t in range(1, T + 1):
    stack = []
    V, E = map(int, input().split())
    matrix = [[0] * (V + 1) for i in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        a, b = map(int, input().split())
        matrix[a][b] = 1

    start, end = map(int, input().split())
    if end in dfs(start):
        res = 1
    else:
        res = 0
    print("#{} {}".format(t, res))