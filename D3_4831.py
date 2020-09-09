T = int(input())
for i in range(1, T+1) :
    K, N, M = map(int, input().split())
    M_info = list(map(int, input().split()))

    station = [0] * (N+1)
    for j in M_info :
        station[j] += 1
    # 정류장 완성~ 충전기있으면 1 없으면 0

    cnt = 0
    a = 0 # 충전하고 다시 출발하는 지점으로 a라는 변수활용
    b = K # 다시 출발했을 때 K만큼 갈수 있는 지점을 표시하기 위해 변수 활용
    while True:
        bye = 0
        for l in range(a+1, b+1) : # 앞에서 부터 충전소가 있으면 출발점을 그곳을 변경 K까지 반복후 최후의 것만 사용
            if station[l] == 1 :
                a = l
            else :
                bye += 1
        if bye == K : # 출발지점부터 K정류장 내에 충전소가 없어서 bye가 K번 쌓이면 0을 출력
            cnt = 0
            break
        cnt += 1
        b = K+a # 시작점이 바뀌었으니 끝점도 바뀌어야 한다.
        if b >= N : # 끝점이 N보다 커지면 더이상 충전을 안해도 된다.
            break
    print(f'#{i} {cnt}')

