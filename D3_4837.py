T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # 부분집합을 list로 받아오자
    li = []
    # 2차원 list로 받아오자
    li_li = []
    # 전에 배웠던 부분집합 만들기
    for i in range(1 << len(A)):
        for j in range(len(A)):
            if i & (1 << j):
                li += [A[j]]
        li_li += [li]
        li = []

    # 원소개수가 N이고 합이 K면 cnt에 1을 추가한다. 없으면 0으로.
    cnt = 0
    for k in li_li:
        if len(k) == N:
            if sum(k) == K:
                cnt += 1

    print(f'#{t} {cnt}')