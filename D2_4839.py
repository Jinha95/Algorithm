def binaryserch(p, key):
    # 시작페이지
    start = 1
    # 끝페이지
    end = p
    # count 가 높으면 진다
    count = 0
    while start <= end:
        index = (start + end) // 2
        count += 1
        # 같으면 끝내고
        if index == key:
            return count
        # 크면 시작점 다시잡고
        elif index < key:
            start = index
        # 작으면 끝점 다시잡고
        elif index > key:
            end = index
    return -1


T = int(input())
for t in range(1, T + 1):
    p, a, b = map(int, input().split())
    a_c = binaryserch(p, a)
    b_c = binaryserch(p, b)
    result = ''
    if a_c < b_c:
        result = 'A'
    elif a_c > b_c:
        result = 'B'
    else:
        result = '0'

    print(f"#{t} {result}")