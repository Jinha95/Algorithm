def cal(temp):
    global cnt
    if len(tree[temp]) == 0:
        return cnt
    length = len(tree[temp])
    cnt += length
    for z in range(length):
        cal(tree[temp][z])


T = int(input())
for t in range(1, T+1):
    # V 정점 총 수 , E 간선 총 수, 공통조상 찾을 A B 정점
    V, E, A, B = map(int, input().split())
    info = list(map(int, input().split()))
    tree = [[] for _ in range(V+1)]
    # tree 의 index = 정점 value = 자식정점
    for i in range(0, 2*E, 2):
        tree[info[i]].append(info[i+1])
    # print(tree)
    a = A
    resultA = []
    while a > 1:
        for i in range(len(tree)):
            if a in tree[i]:
                a = i
                resultA.append(a)
    b = B
    resultB = []
    while b > 1:
        for i in range(len(tree)):
            if b in tree[i]:
                b = i
                resultB.append(b)

    q = 0 # q는 그냥 break 할라고 만들어놓음. break 바로 못하면 메모리 터져서 에러남
    for i in range(len(resultA)):
        for j in range(len(resultB)):
            if resultA[i] == resultB[j]:
                parent = resultB[j]
                q = 1
                break
        if q == 1:
            break

    cnt = 1
    cal(parent)
    print(f'#{t} {parent} {cnt}')