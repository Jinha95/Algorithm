def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(E)]
    p = [0] * (V + 1)

    edges = sorted(edges, key=lambda x: x[2])

    for i in range(V + 1):
        make_set(i)
    ans = 0
    cnt = 0  # 간선을 V개 선택
    idx = 0

    while cnt < V:
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            cnt += 1  # 간선을 선택했으므로 # union 했다는 뜻은 해당 간선을 선택했다는 뜻
            ans += edges[idx][2]
        idx += 1

    print("#{} {}".format(tc, ans))