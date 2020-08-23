T = int(input())
for i in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for j in A :
        for l in A:
            b = abs(j-l)
            B += [b]
    maxv = B[0]
    for k in range(1, len(B)):
        if maxv < B[k] :
            maxv = B[k]
    print(f'#{i} {maxv}')
