for t in range(1, 11):
    t = int(input())
    li = [list(map(str, input())) for _ in range(100)]

    length = 1
    for lili in li:
        for M in range(100, length, -1):
            if length > M:
                break
            for k in range(100-M+1):
                if lili[k:M+k] == lili[k:M+k][::-1]:
                    if len(lili[k:M+k]) > length:
                        length = len(lili[k:M+k])

    lilili = []
    lililili = ''
    for x in range(100):
        for y in li:
            lililili += y[x]
        lilili += [lililili]
        lililili =''

    for j in lilili:
        for M in range(100, length, -1):
            if length > M:
                break
            for k in range(100-M+1):
                if j[k:M+k] == j[k:M+k][::-1]:
                    if len(j[k:M+k]) > length:
                        length = len(j[k:M+k])

    print(f'#{t} {length}')