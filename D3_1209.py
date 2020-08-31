for i in range(1, 11):
    test_number = int(input())
    li = []     # 1차 리스트
    for j in range(100):
        li_li = list(map(int, input().split()))     # 2차 리스트
        li += [li_li]   # 2차원 리스트 완성

    max_sum = 0     # 맥스썸 값에 for 반복 한번마다 최대치만 가지고 간다
    for k in range(100):
        sum1 = 0
        sum2 = 0
        for l in range(100):    # 가로 한줄, 세로한줄
            sum1 += li[k][l]
            sum2 += li[l][k]
        max_sum = max(sum1, sum2, max_sum)  # 그 중 최대값 계속 갱신

    sum3 = 0
    sum4 = 0
    for m in range(100):    # 대각선 값
        sum3 += li[m][m]
        sum4 += li[m][99-m]
    max_sum = max(sum3, sum4, max_sum)  # 가로 세로중 최대값과 각 대각선 값을 비교

    print(f'#{i} {max_sum}')