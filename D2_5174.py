def dfs(a):
    global cnt
    cnt += 1
    for i in tree[a]:
        dfs(i)

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split()) # 간선의 수, 루트노드
    tree = [[] for _ in range(E+2)]
    li = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        a = int(li[i])
        b = int(li[i + 1])
        tree[a].append(b)
    cnt = 0
    dfs(N)
    print(f'#{t} {cnt}')