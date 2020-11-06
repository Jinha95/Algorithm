def cal(a, b, operindex):
    if operindex == 0:
        return a + b
    elif operindex == 1:
        return a - b
    elif operindex == 2:
        return a * b
    else:
        return int(a / b)

def dfs(idx, result):
    if idx >= M:
        global maxx, minn
        if result > maxx:
            maxx = result
        if result < minn:
            minn = result
        return
    # operator list 길이만큼
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            dfs(idx + 1, cal(result, num[idx + 1], i))
            operator[i] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = N-1
    operator = list(map(int, input().split()))
    num = list(map(int, input().split()))
    maxx = -100000000
    minn = 100000000
    dfs(0, num[0])
    print(f'#{tc} {maxx - minn}')