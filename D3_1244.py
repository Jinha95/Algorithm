def dfs(inx):
    global maxx, num2
    num2 = int(''.join(num))
    if num2 in visit[10-inx]:
        return
    else:
        visit[10-inx].add(num2)
    if inx == 0:
        if num2 > maxx:
            maxx = num2
    else:
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                    num[i], num[j] = num[j], num[i]
                    # inx -= 1
                    # print(type(num))
                    dfs(inx-1)
                    num[j], num[i] = num[i], num[j]

T = int(input())
for tc in range(1, T+1):
    q = list(map(str, input().split()))
    # print(q)
    num = []
    # num => 숫자 조합
    for i in range(len(q[0])):
        num.append((q[0][i]))
    # print(num)
    # num = q[0]
    # t => 몇번 바꿀것인가요
    t = int(q[1])
    maxx = 0
    # 횟수, 초기값
    num2 = int(q[0])
    visit = list(set() for _ in range(11))
    dfs(t)
    print(f'#{tc} {maxx}')
