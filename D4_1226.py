dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, 11):
    result = 0
    testcasenumber = int(input())
    li = [list(input()) for _ in range(16)]

    dfs = [(1, 1)]
    while dfs:
        a, b = dfs.pop()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]

            if 0 <= x < 16 and 0 <= y < 16:
                if li[x][y] == '0':
                    dfs.append((x, y))
                    li[x][y] = '1'
                elif li[x][y] == '3':
                    result = 1
                    break

    print(f'#{tc} {result}')
