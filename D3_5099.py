T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    li = []
    for i in range(N):
        li.append([C[i], i])
    # print(C)
    # print(li)
    k = 0
    while len(li) > 1:
        li[0][0] = li[0][0] // 2

        if li[0][0] == 0:
            if N + k < M:
                li.pop(0)
                li.append([C[N+k], N+k])
                k += 1
            elif N+k >= M:
                li.pop(0)
        else:
            li.append(li.pop(0))
    print(f'#{t} {li[0][1]+1}')