def nemo(x):  # x == 현재 위치
    if x > garo:  # 범위를 벗어남
        return 0
    elif x == garo:  # 끝까지 오면 1 리턴
        return 1
    return nemo(x + 10) + nemo(x + 20) * 2

T = int(input())
for t in range(1, T + 1):
    garo = int(input())
    print(f'#{t} {nemo(0)}')
