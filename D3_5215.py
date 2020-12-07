T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    aktdlTdj = []
    EndEnd = []
    for _ in range(N):
        a, b = map(int, input().split())
        aktdlTdj.append(a)
        EndEnd.append(b)
    # print(aktdlTdj)
    # print(EndEnd)
    result = 0
    for i in range(1<<N):
        aktdlTdj_sum = 0
        EndEnd_sum = 0
        for j in range(N):
            if i & (1<<j):
                aktdlTdj_sum += aktdlTdj[j]
                EndEnd_sum += EndEnd[j]
        if EndEnd_sum <= L:
            result = max(result, aktdlTdj_sum)
    print(f'#{tc} {result}')