def ㅋㅋ(start):
    if visit[start] == 0:
        visit[start] = 1
    q = [start]
    while len(q) > 0:
        a = q.pop(0)
        # print(a)
        for k in range(len(friend[a])):
            if visit[friend[a][k]] == 0:
                q.append(friend[a][k])
                visit[friend[a][k]] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    # print(li)
    visit = [2] + ([0] * N)
    # print(visit)
    friend = list([] for _ in range(N+1))
    for i in range(len(li)):
        if i % 2 == 0:
            friend[li[i]].append(li[i+1])
        else:
            friend[li[i]].append(li[i - 1])
    # print(friend)
    cnt = 0
    for i in range(len(friend)):
            if visit[i] == 0:
                ㅋㅋ(i)
                cnt += 1
    # print(visit)
    if 0 not in visit:
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc} {cnt+1}')