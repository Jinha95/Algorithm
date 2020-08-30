T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    li = []
    result = 0
    for i in range(N):
        lili = list(map(int, input().split()))
        li.append(lili)
        cnt = 0
        for j in range(N):
            if lili[j] == 0:
                cnt = 0
            else:
                cnt += 1
            if j+1 < N and cnt == K and lili[j+1] == 0:
                result += 1
            elif j+1 == N and cnt == K:
                result += 1

    Sero = []
    Sero_lst = []
    for x in range(N):
        for y in li:
            Sero_lst.append(y[x])
        Sero.append(Sero_lst)
        cnt1 = 0
        for z in range(N):
            if Sero_lst[z] == 0:
                cnt1 = 0
            else:
                cnt1 += 1
            if z + 1 < N and cnt1 == K and Sero_lst[z + 1] == 0:
                result += 1
            elif z + 1 == N and cnt1 == K:
                result += 1
        Sero_lst = []

    print(f'#{t} {result}')
