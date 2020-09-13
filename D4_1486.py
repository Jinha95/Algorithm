T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    li = []
    lili = []
    for i in range(1 << len(height)):
        for j in range(len(height)):
            if i & (1 << j):
                li += [height[j]]
        if sum(li) >= B:
            lili += [sum(li)]
        li = []

    result = min(lili) - B
    print(f'#{t} {result}')
