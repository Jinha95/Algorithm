def find(l):
    if l > N+1:
        return 0
    if tree[l] != 0:
        return tree[l]

    first = l*2
    second = (l*2)+1
    tree[l] = find(first)+find(second)
    return tree[l]


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드의 개수, 리프 노드의 개수, 출력할 노드
    tree = [0] * (N + 2)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    sol = find(L)
    print(f'#{t} {sol}')
