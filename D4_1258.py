# 가로
def aaa(i, j):
    count = 1
    dx = j
    while True:
        dx += 1
        if dx >= N: break
        if li[i][dx]:
            count += 1
        else:
            break
    return count

# 세로
def bbb(i, j):
    count = 1
    dy = i
    while True:
        dy += 1
        if dy >= N: break
        if li[dy][j]:
            count += 1
        else:
            break
    return count

# 0으로 바꿈
def ccc(s_y, s_x, e_y, e_x):
    for i in range(s_y, e_y):
        for j in range(s_x, e_x):
            li[i][j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    lili = []
    for i in range(N):
        for j in range(N):
            # 값이 있다면
            if li[i][j]:
                # 가로
                w = aaa(i, j)
                # 세로
                h = bbb(i, j)
                # 0
                ccc(i, j, i + h, j + w)

                lili.append([h, w, h * w])
    # 곱한값 기준으로 오름차순, 다음은 행렬 크기로 오름차순
    lili = sorted(lili, key=lambda x: (x[2], x[0]))

    print('#{} {}'.format(t, len(lili)), end=' ')
    for a, b, _ in lili:
        print('{} {}'.format(a, b), end=' ')
    print()