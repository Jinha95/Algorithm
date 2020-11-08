def merge(a):
    global cnt
    if len(a) == 1:
        return a
    else:
        m = len(a)//2
        left = a[:m]
        right = a[m:]
        left = merge(left)
        right = merge(right)
        idxl = 0
        idxr = 0
        i = 0
        while idxl < len(left) and idxr < len(right):
            if left[idxl] < right[idxr]:
                a[i] = left[idxl]
                idxl += 1
            else:
                a[i] = right[idxr]
                idxr += 1
            i += 1
        if left[-1] > right[-1]:
            cnt += 1
        if idxl < len(left):
            a[i:] = left[idxl:]
        if idxr < len(right):
            a[i:] = right[idxr:]
    return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    A = merge(li)
    print(f'#{tc} {A[N//2]} {cnt}')