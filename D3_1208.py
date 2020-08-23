for i in range(1, 11) :
    dump = int(input())
    height = list(map(int, input().split()))
    height.sort()

    for j in range(dump) :
        height[0] += 1
        height[-1] -= 1
        height.sort()
    z = height[-1] - height[0]

    print(f'#{i} {z}')