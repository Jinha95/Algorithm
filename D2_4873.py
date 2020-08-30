T = int(input())
for t in range(1, T+1):
    li = list(map(str, input()))

    start = 1
    while start != len(li):
        if li[start] == li[start-1]:
            del li[start-1:start+1]
            start = 1
        else:
            start += 1

    print(f'#{t} {len(li)}')