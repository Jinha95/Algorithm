def function(n, p):
    global result
    if p <= result:
        # p가 result보다 작다면 더 해볼것도 없음 어차피 더 작아짐
        return
    if n == N and p > result:
        # 다 함
        result = p
        return
    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                function(n+1, p*li[i][n]/100)
                visit[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = []
    for _ in range(N):
        lili = list(map(int, input().split()))
        li.append(lili)
    # print(li)
    visit = [0]*N
    result = 0
    num = 0
    now_p = 1
    function(num, now_p)
    print("#{} {:.6f}".format(tc, result * 100))