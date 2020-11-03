T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    # print(wi)
    # print(ti)
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    # print(ti)
    # print(wi)

    result = 0

    i = 0
    flag = False
    while 1:
        if i >= len(ti) or flag == True:
            break
        j = 0
        while 1:
            if j == len(wi):
                flag = True
                break
            if ti[i] >= wi[j]:
                a = wi[j]
                result += a
                wi.remove(a)
                # print(i)
                # print(wi)

                i += 1
                break
            else:
                j += 1
    print(f'#{tc} {result}')
