T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    friend = []
    for _ in range(M):
        friend.append(list(map(int, input().split())))
    # print(friend)
    # 0번째 인덱스는 비워두는거. 걍 번호 맞추려고
    visit = list([] for _ in range(N+1))
    # print(visit)
    for i in range(len(friend)):
        visit[friend[i][0]].append(friend[i][1])
        visit[friend[i][1]].append(friend[i][0])
    # print(visit)
    if len(visit[1]) == 0:
        print(f'#{tc} 0')
    else:
        result = []
        for j in range(len(visit[1])):
            result.append(visit[1][j])
        for k in visit[1]:
            for z in range(len(visit[k])):
                result.append(visit[k][z])
        # print(result)
        result = list(set(result))
        # print(result)
        print(f'#{tc} {len(result)-1}')